/**
 * Wilderness Destinations Chatbot Client
 * Handles UI interactions and API communication
 */

class WildernessChatbotClient {
    constructor() {
        this.apiUrl = 'http://localhost:5000/api';
        this.sessionId = this.getOrCreateSessionId();
        this.isOpen = false;

        this.elements = {
            chatWidget: document.getElementById('chatWidget'),
            chatToggle: document.getElementById('chatToggle'),
            chatCloseBtn: document.getElementById('chatCloseBtn'),
            chatMessages: document.getElementById('chatMessages'),
            chatInput: document.getElementById('chatInput'),
            sendBtn: document.getElementById('sendBtn'),
            startChatBtn: document.getElementById('startChatBtn'),
            quickReplies: document.getElementById('quickReplies'),
            notificationBadge: document.querySelector('.notification-badge')
        };

        this.initializeEventListeners();
    }

    getOrCreateSessionId() {
        let sessionId = localStorage.getItem('wilderness_session_id');
        if (!sessionId) {
            sessionId = this.generateUUID();
            localStorage.setItem('wilderness_session_id', sessionId);
        }
        return sessionId;
    }

    generateUUID() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            const r = Math.random() * 16 | 0;
            const v = c === 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    initializeEventListeners() {
        // Toggle chat widget
        this.elements.chatToggle.addEventListener('click', () => this.toggleChat());
        this.elements.chatCloseBtn.addEventListener('click', () => this.closeChat());
        this.elements.startChatBtn.addEventListener('click', () => this.openChat());

        // Send message
        this.elements.sendBtn.addEventListener('click', () => this.sendMessage());
        this.elements.chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });

        // Quick replies
        this.elements.quickReplies.addEventListener('click', (e) => {
            if (e.target.classList.contains('quick-reply-btn')) {
                const message = e.target.getAttribute('data-message');
                this.sendMessage(message);
            }
        });
    }

    toggleChat() {
        if (this.isOpen) {
            this.closeChat();
        } else {
            this.openChat();
        }
    }

    openChat() {
        this.elements.chatWidget.classList.add('active');
        this.elements.chatToggle.style.display = 'none';
        this.isOpen = true;
        this.hideNotificationBadge();
        this.elements.chatInput.focus();
    }

    closeChat() {
        this.elements.chatWidget.classList.remove('active');
        this.elements.chatToggle.style.display = 'flex';
        this.isOpen = false;
    }

    hideNotificationBadge() {
        if (this.elements.notificationBadge) {
            this.elements.notificationBadge.style.display = 'none';
        }
    }

    async sendMessage(messageText = null) {
        const message = messageText || this.elements.chatInput.value.trim();

        if (!message) return;

        // Clear input
        this.elements.chatInput.value = '';

        // Add user message to chat
        this.addMessage(message, 'user');

        // Show typing indicator
        this.showTypingIndicator();

        try {
            // Call API
            const response = await fetch(`${this.apiUrl}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            // Remove typing indicator
            this.removeTypingIndicator();

            if (data.success) {
                this.handleBotResponse(data.response);
            } else {
                this.addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }

        } catch (error) {
            console.error('Error sending message:', error);
            this.removeTypingIndicator();
            this.addMessage('Unable to connect to the server. Please check if the backend is running.', 'bot');
        }
    }

    handleBotResponse(response) {
        const { type, message, camps, cta, form_fields } = response;

        // Add main message
        if (message) {
            this.addMessage(message, 'bot');
        }

        // Handle different response types
        switch (type) {
            case 'recommendations':
            case 'destination_info':
            case 'search_results':
                if (camps && camps.length > 0) {
                    this.addCampCards(camps);
                }
                break;

            case 'lead_gen_form':
                if (form_fields) {
                    this.addEnquiryForm(form_fields);
                }
                break;
        }

        // Add CTA if present
        if (cta) {
            this.addMessage(cta, 'bot');
        }
    }

    addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;

        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.innerHTML = sender === 'bot'
            ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>'
            : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4M12 8h.01"></path></svg>';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';

        // Split text into paragraphs
        const paragraphs = text.split('\n').filter(p => p.trim());
        paragraphs.forEach(p => {
            const pElement = document.createElement('p');
            pElement.textContent = p;
            contentDiv.appendChild(pElement);
        });

        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);

        this.elements.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    addCampCards(camps) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message bot-message';

        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';

        camps.forEach(camp => {
            const campCard = document.createElement('div');
            campCard.className = 'camp-card';

            campCard.innerHTML = `
                <h4>${camp.name}</h4>
                <p class="camp-location">📍 ${camp.region}, ${camp.country}</p>
                <p>${camp.description}</p>
                <div class="camp-highlights">
                    ${camp.highlights.slice(0, 3).map(h => `<span class="highlight-tag">${h}</span>`).join('')}
                </div>
            `;

            contentDiv.appendChild(campCard);
        });

        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);

        this.elements.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    addEnquiryForm(fields) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message bot-message';

        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';

        const form = document.createElement('form');
        form.className = 'enquiry-form';
        form.id = 'enquiryForm';

        fields.forEach(field => {
            const formGroup = document.createElement('div');
            formGroup.className = 'form-group';

            const label = document.createElement('label');
            label.textContent = field.label + (field.required ? ' *' : '');
            label.setAttribute('for', field.name);

            let input;
            if (field.type === 'textarea') {
                input = document.createElement('textarea');
            } else {
                input = document.createElement('input');
                input.type = field.type;
            }

            input.id = field.name;
            input.name = field.name;
            input.required = field.required;

            formGroup.appendChild(label);
            formGroup.appendChild(input);
            form.appendChild(formGroup);
        });

        const submitBtn = document.createElement('button');
        submitBtn.type = 'submit';
        submitBtn.className = 'submit-button';
        submitBtn.textContent = 'Send Enquiry';
        form.appendChild(submitBtn);

        form.addEventListener('submit', (e) => this.handleEnquirySubmit(e));

        contentDiv.appendChild(form);
        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);

        this.elements.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    async handleEnquirySubmit(e) {
        e.preventDefault();

        const form = e.target;
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Disable form
        const submitBtn = form.querySelector('.submit-button');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';

        try {
            const response = await fetch(`${this.apiUrl}/enquiry`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.success) {
                // Remove form
                form.remove();

                // Add success message
                this.addMessage(result.result.message, 'bot');
            } else {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Send Enquiry';
                alert('Failed to submit enquiry. Please try again.');
            }

        } catch (error) {
            console.error('Error submitting enquiry:', error);
            submitBtn.disabled = false;
            submitBtn.textContent = 'Send Enquiry';
            alert('Unable to connect to the server. Please try again.');
        }
    }

    showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-message';
        typingDiv.id = 'typingIndicator';

        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';

        const typingIndicator = document.createElement('div');
        typingIndicator.className = 'typing-indicator';
        typingIndicator.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';

        contentDiv.appendChild(typingIndicator);
        typingDiv.appendChild(avatarDiv);
        typingDiv.appendChild(contentDiv);

        this.elements.chatMessages.appendChild(typingDiv);
        this.scrollToBottom();
    }

    removeTypingIndicator() {
        const typingIndicator = document.getElementById('typingIndicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    scrollToBottom() {
        this.elements.chatMessages.scrollTop = this.elements.chatMessages.scrollHeight;
    }
}

// Initialize chatbot when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const chatbot = new WildernessChatbotClient();
    console.log('🌍 Wilderness Destinations Chatbot initialized');
});

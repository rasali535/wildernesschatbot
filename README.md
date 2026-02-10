# 🌍 Wilderness Destinations Concierge Chatbot

A high-end, AI-powered safari concierge chatbot for **Wilderness Destinations** - helping travelers discover luxury wilderness experiences across 55+ camps in 8 African countries.

## 🦁 Features

### Core Functionality
- **Intelligent Intent Recognition** - Understands natural language queries about destinations, experiences, and interests
- **Safari Specialist Mode** - Personalized recommendations based on traveler preferences:
  - Big cat viewing (Okavango Delta)
  - Gorilla trekking (Rwanda)
  - Star bed experiences (Namibia)
  - Mokoro trips (Botswana)
  - Sustainable honeymoons
  - And more...
- **Knowledge Base** - Comprehensive data on 55+ camps across:
  - 🇧🇼 Botswana (Okavango Delta, Linyanti)
  - 🇷🇼 Rwanda (Volcanoes National Park)
  - 🇳🇦 Namibia (Sossusvlei)
  - 🇰🇪 Kenya (Maasai Mara)
  - 🇿🇲 Zambia (South Luangwa)
  - 🇿🇼 Zimbabwe (Hwange)
  - 🇹🇿 Tanzania
  - 🇿🇦 South Africa (KwaZulu-Natal)
- **Lead Generation** - Seamless enquiry workflow connecting travelers with safari specialists
- **Wilderness24 Integration** - Information about 24/7 on-the-ground safety support

### Technical Highlights
- **Backend**: Python with Flask API
- **Frontend**: Vanilla HTML/CSS/JavaScript with premium aesthetics
- **Intent Recognition**: Pattern-based NLP for understanding user queries
- **Session Management**: Persistent conversation history
- **RESTful API**: Clean endpoints for chat, enquiries, and camp data

### Design & UX
- **Premium Brand Aesthetics**: Earthy color palette (forest greens, warm earth tones, luxury gold)
- **Sophisticated Animations**: Smooth transitions, micro-interactions, floating elements
- **Glassmorphism Effects**: Modern, elegant UI components
- **Responsive Design**: Mobile-first approach, works on all devices
- **Accessibility**: WCAG compliant, reduced motion support

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Modern web browser

### Installation

1. **Clone or navigate to the project directory**
```bash
cd C:\Users\user\.gemini\antigravity\scratch\wilderness-chatbot
```

2. **Install Python dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Start the Flask backend**
```bash
python app.py
```
The API will be running at `http://localhost:5000`

4. **Open the frontend**
Open `frontend/index.html` in your web browser, or serve it with a simple HTTP server:
```bash
cd ../frontend
python -m http.server 8000
```
Then visit `http://localhost:8000`

## 📡 API Endpoints

### POST `/api/chat`
Send a chat message and receive bot response
```json
{
  "message": "I want to see big cats",
  "session_id": "optional-session-id"
}
```

### POST `/api/enquiry`
Submit a traveler enquiry
```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "travel_dates": "June 2026",
  "interests": "Big cat viewing and mokoro trips",
  "group_size": 2
}
```

### GET `/api/camps`
Get camp information
- Query params: `?q=search_term` or `?country=Botswana`

### GET `/api/health`
Health check endpoint

## 🧪 Testing the Chatbot

Try these example queries:
- "I want to see big cats"
- "Tell me about gorilla trekking in Rwanda"
- "I'm looking for a sustainable honeymoon"
- "What camps do you have in Botswana?"
- "I want to sleep under the stars"
- "Show me mokoro experiences"
- "I'd like to speak to a specialist"

## 🎨 Brand Guidelines

### Color Palette
- **Primary**: `#2C5530` (Deep Forest Green)
- **Secondary**: `#8B7355` (Warm Earth)
- **Accent**: `#C19A6B` (Desert Sand)
- **Gold**: `#D4AF37` (Luxury Gold)
- **Light**: `#F5F1E8` (Warm White)

### Typography
- **Headings**: Cormorant Garamond (serif)
- **Body**: Montserrat (sans-serif)

### Tone of Voice
Professional, knowledgeable, inspiring, and adventurous - reflecting world-leading conservation and hospitality.

## 🔮 Future Enhancements

### Phase 2 (Production Ready)
- [ ] **Web Scraping**: Automated data collection from wildernessdestinations.com
- [ ] **Real API Integration**: Connect to Wilderness Destinations booking system
- [ ] **Advanced NLP**: Integrate with GPT-4 or similar for more nuanced conversations
- [ ] **Image Gallery**: Display high-res camp photos in chat
- [ ] **Availability Checking**: Real-time camp availability
- [ ] **Multi-language Support**: French, German, Spanish
- [ ] **Voice Interface**: Voice-to-text input
- [ ] **Analytics Dashboard**: Track popular destinations and conversion rates

### Phase 3 (Advanced Features)
- [ ] **Virtual Tours**: 360° camp previews
- [ ] **Itinerary Builder**: Multi-camp safari planning
- [ ] **Price Calculator**: Dynamic pricing based on dates and group size
- [ ] **Weather Integration**: Best time to visit recommendations
- [ ] **Wildlife Sighting Reports**: Real-time updates from camps
- [ ] **Conservation Impact**: Show traveler's contribution to conservation

## 🌟 Camp Highlights

### Featured Camps (Currently in Knowledge Base)
1. **Mombo Camp** - Okavango Delta, Botswana (Best big cat viewing)
2. **Bisate Lodge** - Rwanda (Gorilla trekking & reforestation)
3. **Little Kulala** - Namibia (Iconic star beds)
4. **DumaTau** - Linyanti, Botswana (Massive elephant herds)
5. **Sanctuary Chief's Camp** - Okavango Delta, Botswana
6. **Vumbura Plains** - Okavango Delta, Botswana
7. **Rocktail Beach Camp** - South Africa (Marine conservation)
8. **Angama Mara** - Kenya (Great Migration)
9. **Chinzombo** - Zambia (Walking safari pioneer)
10. **Linkwasha Camp** - Zimbabwe (Painted dog conservation)

## 📝 Project Structure

```
wilderness-chatbot/
├── backend/
│   ├── chatbot.py          # Core chatbot logic & knowledge base
│   ├── app.py              # Flask API server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Main page with chat widget
│   ├── styles.css          # Premium brand styling
│   └── chatbot.js          # Client-side chat logic
└── README.md               # This file
```

## 🤝 Contributing

This is a demonstration project. For production deployment:
1. Replace mock camp data with real API integration
2. Implement proper authentication and rate limiting
3. Add comprehensive error handling and logging
4. Set up monitoring and analytics
5. Deploy to production infrastructure

## 📄 License

This is a demonstration project created for Wilderness Destinations.

## 🙏 Acknowledgments

- **Wilderness Destinations** - For their incredible conservation and hospitality work across Africa
- **Botswana Tourism** - For supporting sustainable safari experiences
- **Conservation Partners** - For protecting Africa's wilderness and wildlife

---

**Built with ❤️ for Africa's Wilderness**

*"Our purpose is to conserve and restore Africa's wilderness and wildlife for the benefit of all."*

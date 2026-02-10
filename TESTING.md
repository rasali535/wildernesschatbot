# 🧪 Testing Guide - Wilderness Destinations Chatbot

## Quick Start Testing

### Step 1: Start the Backend Server

Open a terminal and run:

```bash
cd C:\Users\user\.gemini\antigravity\scratch\wilderness-chatbot\backend
python app.py
```

You should see:

```
🌍 Wilderness Destinations Chatbot API Starting...
📍 Server running on testhttp://localhost:5000
🦁 Ready to help travelers discover Africa's wilderness!
```

### Step 2: Open the Frontend

**Option A: Direct File Access**

- Navigate to: `C:\Users\user\.gemini\antigravity\scratch\wilderness-chatbot\frontend`
- Double-click `index.html` to open in your browser

**Option B: HTTP Server (Recommended)**
Open a second terminal:

```bash
cd C:\Users\user\.gemini\antigravity\scratch\wilderness-chatbot\frontend
python -m http.server 8000
```

Then visit: `http://localhost:8000`

## 🎯 Test Scenarios

### Scenario 1: Big Cat Viewing Interest

**User Input:** "I want to see big cats"

**Expected Response:**

- Bot recommends Mombo Camp in Okavango Delta
- Shows camp card with highlights
- Mentions "exceptional predator viewing"
- Offers to provide more details or connect with specialist

### Scenario 2: Gorilla Trekking

**User Input:** "Tell me about gorilla trekking in Rwanda"

**Expected Response:**

- Bot recommends Bisate Lodge
- Highlights mountain gorilla encounters
- Mentions reforestation project
- Shows Rwanda's Volcanoes National Park location

### Scenario 3: Sustainable Honeymoon

**User Input:** "I'm looking for a sustainable honeymoon"

**Expected Response:**

- Bot recommends intimate camps (max 12-20 guests)
- Highlights sustainability pillars
- Shows camps like Bisate Lodge, Chinzombo
- Emphasizes conservation programs

### Scenario 4: Star Bed Experience

**User Input:** "I want to sleep under the stars"

**Expected Response:**

- Bot recommends Little Kulala in Namibia
- Highlights star bed experience
- Mentions Sossusvlei desert location
- Shows desert-adapted wildlife

### Scenario 5: Country-Specific Query

**User Input:** "What camps do you have in Botswana?"

**Expected Response:**

- Lists multiple Botswana camps:
  - Mombo Camp (Okavango Delta)
  - DumaTau (Linyanti)
  - Sanctuary Chief's Camp (Okavango Delta)
  - Vumbura Plains (Okavango Delta)
- Shows different regions and experiences

### Scenario 6: Mokoro Experience

**User Input:** "Show me mokoro trips"

**Expected Response:**

- Recommends Okavango Delta camps
- Explains traditional mokoro canoe experience
- Shows camps: Mombo, Chief's Camp, Vumbura Plains

### Scenario 7: Lead Generation

**User Input:** "I'd like to speak to a specialist"

**Expected Response:**

- Bot displays enquiry form with fields:
  - Full Name (required)
  - Email Address (required)
  - Phone Number (optional)
  - Preferred Travel Dates (optional)
  - Interests (optional)
  - Number of Travelers (optional)
- Form submits to `/api/enquiry` endpoint
- Success message mentions Wilderness24 support

## 🎨 UI/UX Testing Checklist

### Visual Design

- [ ] Hero section displays with gradient background
- [ ] "Discover Africa's Wilderness" title is prominent
- [ ] Features grid shows 4 cards (Big Cats, Gorillas, Star Beds, Mokoro)
- [ ] Color palette matches brand (forest green, earth tones, gold)
- [ ] Typography uses Cormorant Garamond for headings
- [ ] Typography uses Montserrat for body text

### Chat Widget

- [ ] Chat toggle button appears in bottom-right corner
- [ ] Notification badge shows "1" initially
- [ ] Clicking toggle opens chat widget
- [ ] Chat header shows "Safari Specialist" with online status
- [ ] Green pulsing dot indicates online status
- [ ] Initial greeting message appears
- [ ] Quick reply buttons are visible and clickable

### Interactions

- [ ] Clicking quick reply buttons sends message
- [ ] Typing in input field works smoothly
- [ ] Send button is clickable
- [ ] Pressing Enter sends message
- [ ] Typing indicator appears while waiting for response
- [ ] Messages slide in with animation
- [ ] Chat scrolls to bottom automatically
- [ ] User messages appear on right (green background)
- [ ] Bot messages appear on left (white background)

### Camp Cards

- [ ] Camp cards display with camp name
- [ ] Location shows with 📍 emoji
- [ ] Description is readable
- [ ] Highlight tags appear below description
- [ ] Cards have hover effect (lift up slightly)
- [ ] Cards have subtle shadow

### Enquiry Form

- [ ] Form appears when requesting specialist
- [ ] All fields render correctly
- [ ] Required fields marked with asterisk
- [ ] Submit button is styled correctly
- [ ] Form validation works
- [ ] Success message appears after submission
- [ ] Form is removed after successful submission

### Responsive Design

- [ ] Works on desktop (1920x1080)
- [ ] Works on tablet (768px width)
- [ ] Works on mobile (375px width)
- [ ] Chat widget goes full-screen on mobile
- [ ] Features grid stacks on mobile
- [ ] Text remains readable at all sizes

### Animations

- [ ] Hero content fades in on load
- [ ] Feature icons float gently
- [ ] Buttons have hover effects
- [ ] Messages slide in smoothly
- [ ] Typing indicator animates
- [ ] Status dot pulses
- [ ] Smooth transitions throughout

## 🔧 API Testing

### Test Chat Endpoint

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I want to see big cats",
    "session_id": "test-session-123"
  }'
```

**Expected Response:**

```json
{
  "success": true,
  "session_id": "test-session-123",
  "response": {
    "type": "recommendations",
    "message": "For exceptional big cat viewing...",
    "camps": [...],
    "cta": "Would you like to know more..."
  }
}
```

### Test Enquiry Endpoint

```bash
curl -X POST http://localhost:5000/api/enquiry \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Doe",
    "email": "john@example.com",
    "interests": "Big cat viewing"
  }'
```

### Test Camps Endpoint

```bash
# Get all camps
curl http://localhost:5000/api/camps

# Search camps
curl "http://localhost:5000/api/camps?q=gorilla"

# Filter by country
curl "http://localhost:5000/api/camps?country=Botswana"
```

### Test Health Endpoint

```bash
curl http://localhost:5000/api/health
```

## 🐛 Common Issues & Solutions

### Issue: Chat widget doesn't open

**Solution:** Check browser console for JavaScript errors. Ensure chatbot.js is loaded.

### Issue: Messages not sending

**Solution:**

1. Verify backend is running on port 5000
2. Check browser console for CORS errors
3. Ensure Flask-CORS is installed

### Issue: Styling looks broken

**Solution:**

1. Verify styles.css is loaded
2. Check Google Fonts are loading
3. Clear browser cache

### Issue: API returns 404

**Solution:**

1. Confirm backend server is running
2. Check API URL in chatbot.js (should be <http://localhost:5000/api>)
3. Verify endpoint paths in app.py

### Issue: Form submission fails

**Solution:**

1. Check browser console for errors
2. Verify all required fields are filled
3. Check backend logs for errors

## 📊 Performance Benchmarks

### Expected Response Times

- Chat message processing: < 100ms
- Camp search: < 50ms
- Form submission: < 200ms
- Initial page load: < 2s

### Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

## 🎓 Advanced Testing

### Load Testing

Test with multiple concurrent users:

```python
# Use locust or similar tool
# Target: 100 concurrent users
# Expected: < 500ms response time
```

### Accessibility Testing

- [ ] Screen reader compatible
- [ ] Keyboard navigation works
- [ ] Color contrast meets WCAG AA
- [ ] Focus indicators visible
- [ ] Alt text on images

### Security Testing

- [ ] Input sanitization
- [ ] XSS prevention
- [ ] CSRF protection (for production)
- [ ] Rate limiting (for production)

## 📝 Test Results Template

```
Test Date: __________
Tester: __________
Browser: __________
OS: __________

Scenario Tests:
[ ] Big Cat Viewing - PASS/FAIL
[ ] Gorilla Trekking - PASS/FAIL
[ ] Sustainable Honeymoon - PASS/FAIL
[ ] Star Beds - PASS/FAIL
[ ] Country Query - PASS/FAIL
[ ] Mokoro Experience - PASS/FAIL
[ ] Lead Generation - PASS/FAIL

UI/UX Tests:
[ ] Visual Design - PASS/FAIL
[ ] Chat Widget - PASS/FAIL
[ ] Interactions - PASS/FAIL
[ ] Camp Cards - PASS/FAIL
[ ] Enquiry Form - PASS/FAIL
[ ] Responsive Design - PASS/FAIL
[ ] Animations - PASS/FAIL

Notes:
_________________________________
_________________________________
```

## 🚀 Next Steps After Testing

1. **Document Bugs**: Create issues for any failures
2. **Performance Optimization**: Address any slow responses
3. **User Feedback**: Gather feedback from test users
4. **Iterate**: Implement improvements based on findings
5. **Production Prep**: Add monitoring, logging, analytics

---

**Happy Testing! 🦁🌍**

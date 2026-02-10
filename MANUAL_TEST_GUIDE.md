# 🧪 Manual Testing Guide

## ✅ Servers Status

Both servers are **RUNNING** and ready for testing:

- **Backend API:** <http://localhost:5000> ✅
- **Frontend:** <http://localhost:8000> ✅

---

## 🚀 How to Test the Chatbot

### Step 1: Open the Chatbot

**Open your web browser** (Chrome, Firefox, Edge, or Safari) and navigate to:

```
http://localhost:8000
```

You should see the **Wilderness Destinations** homepage with:

- A beautiful hero section with "Discover Africa's Wilderness"
- Four feature cards (Big Cats, Gorillas, Star Beds, Mokoro)
- A floating chat button in the bottom-right corner

---

## 🎯 Test Scenarios

### Test 1: Open the Chat Widget

1. **Click** the floating chat button (💬) in the bottom-right corner
2. The chat widget should slide open
3. You should see:
   - Green gradient header with "Safari Specialist"
   - Online status indicator (green pulsing dot)
   - Welcome message from the bot
   - Quick reply buttons (🦁 Big Cats, 🦍 Gorillas, 💚 Sustainable, ⭐ Star Beds)

**Expected Result:** Chat opens smoothly with welcome message

---

### Test 2: Big Cat Query

1. **Click** the "🦁 Big Cats" quick reply button
2. Wait for the bot response (2-3 seconds)
3. You should see:
   - Bot message about big cat viewing
   - Camp card(s) showing **Mombo Camp**
   - Location: Okavango Delta, Botswana
   - Highlights like "Best big cat viewing in Africa"

**Expected Result:** Bot recommends Mombo Camp with details

---

### Test 3: Gorilla Trekking Query

1. **Type** in the chat input: `Tell me about gorilla trekking`
2. **Click** the send button (📤) or press Enter
3. Wait for response
4. You should see:
   - Bot message about gorilla trekking
   - **Bisate Lodge** camp card
   - Location: Volcanoes National Park, Rwanda
   - Highlights about mountain gorillas and reforestation

**Expected Result:** Bot recommends Bisate Lodge in Rwanda

---

### Test 4: Sustainable Honeymoon

1. **Type:** `I'm looking for a sustainable honeymoon`
2. **Send** the message
3. You should see:
   - Bot reasoning about sustainable camps
   - Multiple camp recommendations
   - Focus on intimate camps with conservation programs

**Expected Result:** Multiple eco-friendly camp recommendations

---

### Test 5: Star Beds Experience

1. **Type:** `I want to sleep under the stars`
2. **Send** the message
3. You should see:
   - **Little Kulala** camp in Namibia
   - Star bed experience highlighted
   - Desert location details

**Expected Result:** Little Kulala recommendation

---

### Test 6: Country-Specific Query

1. **Type:** `What camps do you have in Botswana?`
2. **Send** the message
3. You should see:
   - Multiple Botswana camps listed:
     - Mombo Camp (Okavango Delta)
     - DumaTau (Linyanti)
     - Sanctuary Chief's Camp (Okavango Delta)
     - Vumbura Plains (Okavango Delta)

**Expected Result:** 4 Botswana camps displayed

---

### Test 7: Lead Generation (Enquiry Form)

1. **Type:** `I'd like to speak to a specialist`
2. **Send** the message
3. You should see:
   - Bot message about connecting you with specialists
   - An enquiry form with fields:
     - Full Name (required)
     - Email Address (required)
     - Phone Number (optional)
     - Preferred Travel Dates (optional)
     - Interests (optional)
     - Number of Travelers (optional)
   - "Send Enquiry" button

4. **Fill out the form** with test data:
   - Name: Test User
   - Email: <test@example.com>
   - Interests: Big cat viewing

5. **Click** "Send Enquiry"
6. You should see:
   - Success message
   - Mention of Wilderness24 safety support
   - Reference ID

**Expected Result:** Form submits successfully with confirmation

---

## 🎨 Visual Checks

### Design Elements to Verify

- [ ] **Colors:** Forest green (#2C5530), earth tones, gold accents
- [ ] **Typography:** Elegant serif headings, clean sans-serif body text
- [ ] **Animations:**
  - Hero section fades in on load
  - Feature icons float gently
  - Messages slide in smoothly
  - Typing indicator animates (three bouncing dots)
  - Status dot pulses
- [ ] **Responsiveness:** Resize browser window to test mobile view
- [ ] **Shadows:** Subtle shadows on cards and chat widget
- [ ] **Rounded Corners:** Smooth rounded edges throughout

---

## 🔍 Things to Look For

### ✅ Good Signs

- Chat opens instantly when clicking toggle
- Messages appear smoothly
- Camp cards are beautifully formatted
- Quick reply buttons work
- Form validation works (try submitting empty form)
- Typing indicator shows while waiting
- Scroll works in chat messages
- Colors match brand (earthy greens, gold)

### ⚠️ Potential Issues

- If chat doesn't open: Check browser console (F12) for errors
- If messages don't send: Verify backend is running on port 5000
- If styling looks broken: Clear browser cache (Ctrl+Shift+R)
- If API errors: Check backend terminal for error messages

---

## 🖥️ Browser Console Testing

Press **F12** to open Developer Tools, then:

1. Go to **Console** tab
2. You should see: `🌍 Wilderness Destinations Chatbot initialized`
3. Send a message and watch for API calls in **Network** tab
4. Look for POST requests to `http://localhost:5000/api/chat`

---

## 📱 Mobile Testing

1. Resize browser window to mobile size (375px width)
2. Chat widget should go **full-screen**
3. Features should **stack vertically**
4. Text should remain **readable**
5. Touch targets should be **large enough**

---

## 🎥 What You Should Experience

### The Full User Journey

1. **Land on page** → Beautiful hero with "Discover Africa's Wilderness"
2. **Scroll down** → See 4 feature cards with floating icons
3. **Click chat** → Widget slides open with welcome message
4. **Click quick reply** → Instant message send, typing indicator, then response
5. **See camp card** → Beautiful card with location, description, highlights
6. **Type custom query** → Natural conversation flow
7. **Request specialist** → Form appears seamlessly
8. **Submit form** → Success message with reference ID

---

## 🐛 Troubleshooting

### Chat Widget Not Opening?

- Check browser console for JavaScript errors
- Verify `chatbot.js` is loaded (Network tab)
- Try hard refresh (Ctrl+Shift+R)

### No Bot Response?

- Check backend is running: <http://localhost:5000/api/health>
- Look at backend terminal for errors
- Check browser console for CORS errors

### Styling Issues?

- Verify `styles.css` is loaded
- Check Google Fonts are loading
- Clear browser cache

### Form Not Submitting?

- Fill required fields (marked with *)
- Check browser console for validation errors
- Verify backend `/api/enquiry` endpoint

---

## 📊 Success Criteria

Your test is **SUCCESSFUL** if:

✅ Page loads with beautiful hero section  
✅ Chat widget opens smoothly  
✅ Bot responds to all 7 test queries  
✅ Camp cards display correctly  
✅ Enquiry form appears and submits  
✅ Animations are smooth  
✅ Design matches brand (earthy, premium)  
✅ No console errors  
✅ Mobile view works  

---

## 🎉 After Testing

Once you've verified everything works:

1. **Take screenshots** of your favorite interactions
2. **Customize** the camps/content in `backend/chatbot.py`
3. **Adjust colors** in `frontend/styles.css` if needed
4. **Review** DEPLOYMENT.md for production steps
5. **Share** with stakeholders!

---

## 🆘 Need Help?

If you encounter issues:

1. Check backend terminal for error messages
2. Check browser console (F12) for JavaScript errors
3. Review TESTING.md for detailed troubleshooting
4. Verify both servers are running (ports 5000 and 8000)

---

## 🌍 Enjoy Testing

You're about to experience a **premium safari concierge chatbot** that showcases the best of Africa's wilderness. Have fun exploring! 🦁🌿

**Direct Link:** <http://localhost:8000>

---

**Built with ❤️ for Africa's Wilderness**

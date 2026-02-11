# 🌍 Wilderness Destinations Concierge Chatbot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)

A premium, AI-powered safari concierge chatbot for **Wilderness Destinations** - helping travelers discover luxury wilderness experiences across 55+ camps in 8 African countries.

![Wilderness Chatbot](https://img.shields.io/badge/Status-Production%20Ready-success)

---

## ✨ Features

### 🤖 Intelligent Chatbot

- **Natural Language Understanding** - Recognizes safari-related queries and traveler intent
- **Safari Specialist Mode** - Provides personalized camp recommendations based on interests
- **Smart Recommendations** - Suggests camps for 25+ experiences including:
  - Big cat viewing, gorilla trekking, rhino tracking
  - Helicopter safaris, hot air ballooning, e-biking
  - Star beds, mokoro trips, canoeing adventures
  - Birding (930+ species), stargazing, photography
  - Cultural immersion, wellness safaris, and more
- **Lead Generation** - Seamless enquiry workflow connecting travelers with safari specialists

### 🏕️ Comprehensive Knowledge Base

- **15 Featured Camps** across 8 African countries:
  - 🇧🇼 Botswana (Okavango Delta, Linyanti) - 5 camps
  - 🇷🇼 Rwanda (Volcanoes, Akagera) - 2 camps
  - 🇳🇦 Namibia (Sossusvlei, Skeleton Coast) - 2 camps
  - 🇿🇼 Zimbabwe (Hwange, Mana Pools) - 2 camps
  - 🇿🇲 Zambia (South Luangwa) - 1 camp
  - 🇰🇪 Kenya (Maasai Mara) - 1 camp
  - 🇹🇿 Tanzania (Serengeti) - 1 camp
  - 🇿🇦 South Africa (KwaZulu-Natal) - 1 camp

### 🎨 Premium Design

- **Brand-Perfect Aesthetics** - Earthy color palette (forest greens, warm earth tones, luxury gold)
- **Sophisticated Animations** - Smooth transitions, micro-interactions, floating elements
- **Glassmorphism Effects** - Modern, elegant UI components
- **Responsive Design** - Mobile-first approach, works on all devices
- **Accessibility** - WCAG compliant, keyboard navigation, screen reader support

### ⚙️ Technical Excellence

- **RESTful API** - Clean Flask backend with 4 endpoints
- **Session Management** - Persistent conversation history
- **Production-Ready** - Error handling, logging, comprehensive documentation
- **Scalable Architecture** - Clean separation of concerns

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/rasali535/wildernesschatbot.git
cd wildernesschatbot
```

1. **Install Python dependencies**

```bash
cd backend
pip install -r requirements.txt
```

1. **Start the backend server**

```bash
python app.py
```

The API will be running at `http://localhost:5000`

1. **Open the frontend**

In a new terminal:

```bash
cd ../frontend
python -m http.server 8000
```

Then visit `http://localhost:8000` in your browser

### Using Batch Files (Windows)

- Double-click `start-server.bat` to start the backend
- Double-click `start-frontend.bat` to start the frontend
- Open `http://localhost:8000` in your browser

---

## 🧪 Try It Out

Once the chatbot is running, try these queries:

1. **"I want to see big cats"** → Recommends Mombo Camp in Okavango Delta
2. **"Tell me about gorilla trekking"** → Shows Bisate Lodge in Rwanda
3. **"Show me helicopter safari options"** → Highlights Okavango Delta camps
4. **"I'm interested in rhino tracking"** → Suggests Hoanib and Chinzombo camps
5. **"Tell me about hot air ballooning"** → Shows Little Kulala and Angama Mara
6. **"What camps do you have in Botswana?"** → Lists 5 Botswana camps
7. **"I want to sleep under the stars"** → Highlights star bed experiences
8. **"Show me canoeing experiences"** → Recommends Ruckomechi Camp (Mana Pools)
9. **"I'm looking for birding opportunities"** → Shows camps with 930+ species
10. **"I'd like to speak to a specialist"** → Opens enquiry form

---

## 📡 API Documentation

### Endpoints

#### `POST /api/chat`

Send a chat message and receive bot response

```json
{
  "message": "I want to see big cats",
  "session_id": "optional-session-id"
}
```

#### `POST /api/enquiry`

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

#### `GET /api/camps`

Get camp information

- Query params: `?q=search_term` or `?country=Botswana`

#### `GET /api/health`

Health check endpoint

---

## 🏗️ Project Structure

```
wildernesschatbot/
├── backend/
│   ├── chatbot.py          # Core AI logic & knowledge base
│   ├── app.py              # Flask API server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Main page with chat widget
│   ├── styles.css          # Premium brand styling
│   └── chatbot.js          # Client-side chat logic
├── docs/
│   ├── README.md           # This file
│   ├── TESTING.md          # Testing guide
│   ├── DEPLOYMENT.md       # Production deployment
│   ├── DESIGN_SYSTEM.md    # Visual design docs
│   └── PROJECT_SUMMARY.md  # Complete summary
├── .gitignore
├── START_HERE.md           # Quick start guide
├── start-server.bat        # Backend launcher (Windows)
└── start-frontend.bat      # Frontend launcher (Windows)
```

---

## 🎨 Design System

### Color Palette

- **Primary**: `#2C5530` (Deep Forest Green)
- **Secondary**: `#8B7355` (Warm Earth)
- **Accent**: `#C19A6B` (Desert Sand)
- **Gold**: `#D4AF37` (Luxury Gold)
- **Light**: `#F5F1E8` (Warm White)

### Typography

- **Headings**: Cormorant Garamond (elegant serif)
- **Body**: Montserrat (clean sans-serif)

### Key Animations

- Hero fade-in on page load
- Floating feature icons
- Message slide-in effects
- Typing indicator (bouncing dots)
- Pulsing online status

---

## 🌟 Featured Camps

### Botswana (5 camps)

1. **Mombo Camp** - Okavango Delta (Best big cat viewing, helicopter safaris)
2. **DumaTau** - Linyanti (Massive elephant herds, barge trips)
3. **Sanctuary Chief's Camp** - Okavango Delta (Exclusive island, helicopter safaris)
4. **Vumbura Plains** - Okavango Delta (Water & land activities, stargazing)
5. **Qorokwe Camp** - Okavango Delta (Year-round water, diverse ecosystems)

### Rwanda (2 camps)

1. **Bisate Lodge** - Volcanoes National Park (Gorilla trekking, reforestation, star beds)
2. **Magashi Camp** - Akagera National Park (Big Five safaris, conservation success)

### Namibia (2 camps)

1. **Little Kulala** - Sossusvlei (Iconic star beds, hot air ballooning, e-biking)
2. **Hoanib Skeleton Coast Camp** - Skeleton Coast (Desert elephants, rhino tracking)

### Zimbabwe (2 camps)

1. **Linkwasha Camp** - Hwange National Park (Painted dog conservation, star beds)
2. **Ruckomechi Camp** - Mana Pools (Zambezi canoeing, walking safaris)

### Other Countries

1. **Rocktail Beach Camp** - South Africa (Marine conservation, turtle tracking)
2. **Angama Mara** - Kenya (Great Migration, hot air ballooning)
3. **Chinzombo** - Zambia (Walking safari pioneer, rhino tracking)
4. **Serengeti Under Canvas** - Tanzania (Great Migration tracking, mobile camp)

---

## 📚 Documentation

- **[START_HERE.md](START_HERE.md)** - Quick start guide
- **[TESTING.md](TESTING.md)** - Comprehensive testing guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment guide
- **[DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)** - Visual design documentation
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project summary
- **[MANUAL_TEST_GUIDE.md](MANUAL_TEST_GUIDE.md)** - Manual testing instructions

---

## 🔮 Roadmap

### Phase 2: Production Integration

- [ ] Web scraping from wildernessdestinations.com
- [ ] Real API integration with booking system
- [ ] Advanced NLP with GPT-4
- [ ] High-res image gallery in chat
- [ ] Real-time availability checking
- [ ] Multi-language support (French, German, Spanish)

### Phase 3: Advanced Features

- [ ] 360° virtual camp tours
- [ ] Multi-camp itinerary builder
- [ ] Dynamic pricing calculator
- [ ] Weather integration
- [ ] Real-time wildlife sighting reports
- [ ] Conservation impact dashboard

---

## 🤝 Contributing

This is a demonstration project. For production deployment:

1. Replace mock camp data with real API integration
2. Implement proper authentication and rate limiting
3. Add comprehensive error handling and logging
4. Set up monitoring and analytics
5. Deploy to production infrastructure

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Wilderness Destinations** - For their incredible conservation and hospitality work across Africa
- **Botswana Tourism** - For supporting sustainable safari experiences
- **Conservation Partners** - For protecting Africa's wilderness and wildlife

---

## 📞 Contact

For questions or support, please open an issue on GitHub.

---

## 🌍 About Wilderness Destinations

Wilderness Destinations is a world-leading conservation and hospitality company operating 55+ camps across 8 African countries. Their purpose is to conserve and restore Africa's wilderness and wildlife for the benefit of all.

**Key Pillars:**

- Wildlife Conservation
- Community Development
- Sustainable Tourism
- Carbon Neutral Operations

---

**Built with ❤️ for Africa's Wilderness**

*"Our purpose is to conserve and restore Africa's wilderness and wildlife for the benefit of all."*

---

## 🔗 Links

- **Live Demo**: Coming soon
- **Documentation**: See `/docs` folder
- **Issues**: [GitHub Issues](https://github.com/rasali535/wildernesschatbot/issues)
- **Wilderness Destinations**: [wildernessdestinations.com](https://wildernessdestinations.com)

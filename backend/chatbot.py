"""
Wilderness Destinations Concierge Chatbot Backend
High-end safari and conservation experience advisor
"""

import json
import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Camp:
    """Represents a Wilderness Destinations camp"""
    name: str
    country: str
    region: str
    max_guests: int
    experiences: List[str]
    sustainability_pillars: List[str]
    description: str
    image_url: str
    highlights: List[str]


@dataclass
class UserIntent:
    """Represents parsed user intent"""
    intent_type: str  # 'destination_query', 'experience_search', 'lead_gen', 'general_info'
    entities: Dict[str, any]
    confidence: float


class WildernessKnowledgeBase:
    """Knowledge base of Wilderness Destinations camps and experiences"""
    
    def __init__(self):
        self.camps = self._initialize_camps()
        self.experiences_map = self._build_experiences_map()
        
    def _initialize_camps(self) -> List[Camp]:
        """Initialize camp data - in production, this would be crawled from the website"""
        return [
            Camp(
                name="Mombo Camp",
                country="Botswana",
                region="Okavango Delta",
                max_guests=16,
                experiences=["Big Cat Viewing", "Mokoro Trips", "Game Drives", "Walking Safaris"],
                sustainability_pillars=["Wildlife Conservation", "Community Development", "Carbon Neutral"],
                description="Situated on Mombo Island in the heart of the Okavango Delta, Mombo is renowned for exceptional predator viewing.",
                image_url="/images/mombo-camp.jpg",
                highlights=["Best big cat viewing in Africa", "Exclusive island location", "Year-round water"]
            ),
            Camp(
                name="Bisate Lodge",
                country="Rwanda",
                region="Volcanoes National Park",
                max_guests=12,
                experiences=["Gorilla Trekking", "Golden Monkey Tracking", "Conservation Activities", "Cultural Visits"],
                sustainability_pillars=["Reforestation", "Community Empowerment", "Endangered Species Protection"],
                description="Bisate Lodge offers an unparalleled gorilla trekking experience with a strong focus on conservation and reforestation.",
                image_url="/images/bisate-lodge.jpg",
                highlights=["Mountain gorilla encounters", "Reforestation project", "Amphitheatre setting"]
            ),
            Camp(
                name="Little Kulala",
                country="Namibia",
                region="Sossusvlei",
                max_guests=22,
                experiences=["Star Beds", "Dune Excursions", "Hot Air Ballooning", "Nature Drives"],
                sustainability_pillars=["Desert Conservation", "Solar Power", "Water Conservation"],
                description="Experience the magic of the Namib Desert with iconic star beds and access to the world's highest dunes.",
                image_url="/images/little-kulala.jpg",
                highlights=["Sleep under the stars", "Sossusvlei access", "Desert-adapted wildlife"]
            ),
            Camp(
                name="DumaTau",
                country="Botswana",
                region="Linyanti",
                max_guests=20,
                experiences=["Elephant Viewing", "Game Drives", "Boat Cruises", "Photographic Hides"],
                sustainability_pillars=["Elephant Conservation", "Anti-Poaching", "Habitat Protection"],
                description="DumaTau overlooks the Linyanti River and Osprey Lagoon, famous for large elephant herds.",
                image_url="/images/dumatau.jpg",
                highlights=["Massive elephant herds", "Water-based activities", "Predator sightings"]
            ),
            Camp(
                name="Sanctuary Chief's Camp",
                country="Botswana",
                region="Okavango Delta",
                max_guests=20,
                experiences=["Mokoro Trips", "Game Drives", "Walking Safaris", "Birdwatching"],
                sustainability_pillars=["Wildlife Conservation", "Community Support", "Eco-Tourism"],
                description="Chief's Camp is located on Chief's Island, one of the most exclusive wildlife areas in the Okavango.",
                image_url="/images/chiefs-camp.jpg",
                highlights=["Exclusive Chief's Island", "Diverse wildlife", "Luxury tented suites"]
            ),
            Camp(
                name="Vumbura Plains",
                country="Botswana",
                region="Okavango Delta",
                max_guests=32,
                experiences=["Game Drives", "Mokoro Trips", "Fishing", "Boat Cruises"],
                sustainability_pillars=["Wetland Conservation", "Solar Energy", "Community Partnership"],
                description="Vumbura Plains combines water and land-based activities in a pristine wilderness setting.",
                image_url="/images/vumbura-plains.jpg",
                highlights=["Water and land activities", "Contemporary design", "Excellent game viewing"]
            ),
            Camp(
                name="Rocktail Beach Camp",
                country="South Africa",
                region="KwaZulu-Natal",
                max_guests=28,
                experiences=["Snorkeling", "Turtle Tracking", "Forest Walks", "Beach Activities"],
                sustainability_pillars=["Marine Conservation", "Turtle Protection", "Community Tourism"],
                description="Rocktail offers a unique coastal wilderness experience with pristine beaches and coral reefs.",
                image_url="/images/rocktail-beach.jpg",
                highlights=["Pristine beaches", "Turtle nesting", "Coral reef snorkeling"]
            ),
            Camp(
                name="Angama Mara",
                country="Kenya",
                region="Maasai Mara",
                max_guests=30,
                experiences=["Great Migration", "Game Drives", "Hot Air Ballooning", "Cultural Visits"],
                sustainability_pillars=["Community Education", "Wildlife Protection", "Sustainable Tourism"],
                description="Perched high above the Maasai Mara, Angama offers breathtaking views and front-row seats to the Great Migration.",
                image_url="/images/angama-mara.jpg",
                highlights=["Great Migration viewing", "Spectacular views", "Photographic excellence"]
            ),
            Camp(
                name="Chinzombo",
                country="Zambia",
                region="South Luangwa",
                max_guests=12,
                experiences=["Walking Safaris", "Game Drives", "Night Drives", "Photographic Hides"],
                sustainability_pillars=["Anti-Poaching", "Community Development", "Wildlife Research"],
                description="Chinzombo is an intimate camp on the banks of the Luangwa River, birthplace of the walking safari.",
                image_url="/images/chinzombo.jpg",
                highlights=["Walking safari pioneer area", "Riverfront location", "Intimate luxury"]
            ),
            Camp(
                name="Linkwasha Camp",
                country="Zimbabwe",
                region="Hwange National Park",
                max_guests=18,
                experiences=["Game Drives", "Walking Safaris", "Hide Photography", "Star Gazing"],
                sustainability_pillars=["Painted Dog Conservation", "Habitat Protection", "Community Support"],
                description="Linkwasha overlooks a waterhole in Hwange, offering exceptional wildlife viewing year-round.",
                image_url="/images/linkwasha.jpg",
                highlights=["Painted dog sightings", "Waterhole views", "Diverse wildlife"]
            )
        ]
    
    def _build_experiences_map(self) -> Dict[str, List[str]]:
        """Build a map of experiences to camps offering them"""
        experiences_map = {}
        for camp in self.camps:
            for experience in camp.experiences:
                if experience not in experiences_map:
                    experiences_map[experience] = []
                experiences_map[experience].append(camp.name)
        return experiences_map
    
    def get_camps_by_country(self, country: str) -> List[Camp]:
        """Get all camps in a specific country"""
        return [camp for camp in self.camps if camp.country.lower() == country.lower()]
    
    def get_camps_by_experience(self, experience: str) -> List[Camp]:
        """Get camps offering a specific experience"""
        experience_lower = experience.lower()
        return [camp for camp in self.camps 
                if any(exp.lower() == experience_lower for exp in camp.experiences)]
    
    def search_camps(self, query: str) -> List[Camp]:
        """Search camps by keyword"""
        query_lower = query.lower()
        results = []
        for camp in self.camps:
            if (query_lower in camp.name.lower() or 
                query_lower in camp.description.lower() or
                query_lower in camp.region.lower() or
                any(query_lower in exp.lower() for exp in camp.experiences)):
                results.append(camp)
        return results


class IntentRecognizer:
    """Recognizes user intent from natural language input"""
    
    def __init__(self):
        self.intent_patterns = {
            'big_cats': r'\b(big cats?|lions?|leopards?|cheetahs?|predators?)\b',
            'gorillas': r'\b(gorillas?|primates?|mountain gorillas?|gorilla trekking)\b',
            'elephants': r'\b(elephants?|jumbos?)\b',
            'mokoro': r'\b(mokoro|canoe|canoeing)\b',
            'star_beds': r'\b(star beds?|sleep under stars|sleeping under stars)\b',
            'honeymoon': r'\b(honeymoon|romantic|couples?)\b',
            'sustainable': r'\b(sustainable|sustainability|conservation|eco-friendly|green)\b',
            'luxury': r'\b(luxury|luxurious|high-end|premium|exclusive)\b',
            'migration': r'\b(migration|great migration|wildebeest)\b',
            'walking_safari': r'\b(walking safari|walk|on foot)\b',
            'water_activities': r'\b(water|boat|cruise|fishing|snorkel)\b',
            'beach': r'\b(beach|coast|ocean|marine|sea)\b',
            'country_botswana': r'\b(botswana)\b',
            'country_rwanda': r'\b(rwanda)\b',
            'country_namibia': r'\b(namibia)\b',
            'country_kenya': r'\b(kenya|maasai mara|mara)\b',
            'country_zambia': r'\b(zambia|luangwa)\b',
            'country_zimbabwe': r'\b(zimbabwe|hwange)\b',
            'country_tanzania': r'\b(tanzania|serengeti)\b',
            'country_south_africa': r'\b(south africa)\b',
            'enquire': r'\b(enquire|inquiry|book|contact|speak to|talk to|specialist)\b',
        }
        
    def recognize(self, user_input: str) -> UserIntent:
        """Recognize intent from user input"""
        user_input_lower = user_input.lower()
        entities = {}
        
        # Check for enquiry intent first
        if re.search(self.intent_patterns['enquire'], user_input_lower, re.IGNORECASE):
            return UserIntent(
                intent_type='lead_gen',
                entities={},
                confidence=0.95
            )
        
        # Extract entities
        for key, pattern in self.intent_patterns.items():
            if re.search(pattern, user_input_lower, re.IGNORECASE):
                entities[key] = True
        
        # Determine primary intent
        if any(k.startswith('country_') for k in entities):
            return UserIntent(
                intent_type='destination_query',
                entities=entities,
                confidence=0.9
            )
        elif entities:
            return UserIntent(
                intent_type='experience_search',
                entities=entities,
                confidence=0.85
            )
        else:
            return UserIntent(
                intent_type='general_info',
                entities={},
                confidence=0.6
            )


class SafariSpecialistAgent:
    """Safari specialist mode for personalized recommendations"""
    
    def __init__(self, knowledge_base: WildernessKnowledgeBase):
        self.kb = knowledge_base
        
    def recommend_by_interest(self, intent: UserIntent) -> Tuple[List[Camp], str]:
        """Recommend camps based on user interests"""
        entities = intent.entities
        recommendations = []
        reasoning = ""
        
        # Big cats interest
        if entities.get('big_cats'):
            big_cat_camps = [c for c in self.kb.camps 
                           if 'Big Cat Viewing' in c.experiences or 
                           'big cat' in c.description.lower() or
                           c.name == 'Mombo Camp']
            recommendations.extend(big_cat_camps)
            reasoning += "For exceptional big cat viewing, I recommend camps in the Okavango Delta. "
        
        # Gorilla trekking
        if entities.get('gorillas'):
            gorilla_camps = [c for c in self.kb.camps if 'Gorilla Trekking' in c.experiences]
            recommendations.extend(gorilla_camps)
            reasoning += "For gorilla trekking, Rwanda's Bisate Lodge offers an unforgettable experience. "
        
        # Star beds
        if entities.get('star_beds'):
            star_camps = [c for c in self.kb.camps if 'Star Beds' in c.experiences]
            recommendations.extend(star_camps)
            reasoning += "For sleeping under the stars, Little Kulala in Namibia is unparalleled. "
        
        # Honeymoon + sustainable
        if entities.get('honeymoon') and entities.get('sustainable'):
            honeymoon_camps = [c for c in self.kb.camps 
                             if len(c.sustainability_pillars) >= 3 and c.max_guests <= 20]
            recommendations.extend(honeymoon_camps)
            reasoning += "For a sustainable honeymoon, I recommend intimate camps with strong conservation programs. "
        
        # Mokoro trips
        if entities.get('mokoro'):
            mokoro_camps = [c for c in self.kb.camps if 'Mokoro Trips' in c.experiences]
            recommendations.extend(mokoro_camps)
            reasoning += "For traditional mokoro experiences, the Okavango Delta camps are perfect. "
        
        # Water activities
        if entities.get('water_activities'):
            water_camps = [c for c in self.kb.camps 
                         if any(exp in c.experiences for exp in ['Boat Cruises', 'Mokoro Trips', 'Fishing', 'Snorkeling'])]
            recommendations.extend(water_camps)
            reasoning += "For water-based activities, I recommend camps with river or delta access. "
        
        # Beach/marine
        if entities.get('beach'):
            beach_camps = [c for c in self.kb.camps if 'Beach' in c.name or 'Snorkeling' in c.experiences]
            recommendations.extend(beach_camps)
            reasoning += "For a coastal experience, Rocktail Beach Camp offers pristine beaches and marine life. "
        
        # Country-specific
        for key in entities:
            if key.startswith('country_'):
                country = key.replace('country_', '').replace('_', ' ').title()
                country_camps = self.kb.get_camps_by_country(country)
                recommendations.extend(country_camps)
                reasoning += f"Exploring {country}'s wilderness offerings. "
        
        # Remove duplicates while preserving order
        seen = set()
        unique_recommendations = []
        for camp in recommendations:
            if camp.name not in seen:
                seen.add(camp.name)
                unique_recommendations.append(camp)
        
        if not unique_recommendations:
            # Default recommendations
            unique_recommendations = self.kb.camps[:3]
            reasoning = "Here are some of our most popular camps to get you started. "
        
        return unique_recommendations, reasoning


class WildernessChatbot:
    """Main chatbot orchestrator"""
    
    def __init__(self):
        self.knowledge_base = WildernessKnowledgeBase()
        self.intent_recognizer = IntentRecognizer()
        self.safari_specialist = SafariSpecialistAgent(self.knowledge_base)
        self.conversation_state = {}
        
    def process_message(self, user_id: str, message: str) -> Dict:
        """Process user message and generate response"""
        
        # Initialize user state if new
        if user_id not in self.conversation_state:
            self.conversation_state[user_id] = {
                'step': 'awaiting_details',
                'details': {}
            }
            
        # Handle initial contact details capture
        if self.conversation_state[user_id]['step'] == 'awaiting_details':
            # Store the message as their details (simplistic for now)
            self.conversation_state[user_id]['details']['raw_contact'] = message
            self.conversation_state[user_id]['step'] = 'chatting'
            
            return {
                'type': 'general',
                'message': f"Thank you! It's a pleasure to meet you. Now, let's plan your adventure. What kind of wilderness experience are you dreaming of? (e.g., Big cats, gorilla trekking, or a romantic honeymoon?)",
                'cta': 'Tell me about your dream safari!'
            }
        
        # Recognize intent
        intent = self.intent_recognizer.recognize(message)
        
        # Route to appropriate handler
        if intent.intent_type == 'lead_gen':
            return self._handle_lead_gen(user_id)
        elif intent.intent_type == 'experience_search':
            return self._handle_experience_search(intent)
        elif intent.intent_type == 'destination_query':
            return self._handle_destination_query(intent)
        else:
            return self._handle_general_info(message)
    
    def _handle_experience_search(self, intent: UserIntent) -> Dict:
        """Handle experience-based searches"""
        recommendations, reasoning = self.safari_specialist.recommend_by_interest(intent)
        
        response_text = f"{reasoning}\n\n"
        
        camps_data = []
        for camp in recommendations[:3]:  # Top 3 recommendations
            camps_data.append(asdict(camp))
        
        return {
            'type': 'recommendations',
            'message': response_text,
            'camps': camps_data,
            'cta': 'Would you like to know more about any of these camps, or shall I connect you with one of our safari specialists?'
        }
    
    def _handle_destination_query(self, intent: UserIntent) -> Dict:
        """Handle destination-specific queries"""
        recommendations, reasoning = self.safari_specialist.recommend_by_interest(intent)
        
        camps_data = [asdict(camp) for camp in recommendations]
        
        return {
            'type': 'destination_info',
            'message': reasoning,
            'camps': camps_data,
            'cta': 'Each of these camps offers unique experiences. Would you like detailed information about any specific camp?'
        }
    
    def _handle_lead_gen(self, user_id: str) -> Dict:
        """Handle lead generation / enquiry"""
        return {
            'type': 'lead_gen_form',
            'message': "I'd be delighted to connect you with one of our expert safari specialists! They'll help craft your perfect wilderness adventure.",
            'form_fields': [
                {'name': 'full_name', 'label': 'Full Name', 'type': 'text', 'required': True},
                {'name': 'email', 'label': 'Email Address', 'type': 'email', 'required': True},
                {'name': 'phone', 'label': 'Phone Number', 'type': 'tel', 'required': False},
                {'name': 'travel_dates', 'label': 'Preferred Travel Dates', 'type': 'text', 'required': False},
                {'name': 'interests', 'label': 'What interests you most?', 'type': 'textarea', 'required': False},
                {'name': 'group_size', 'label': 'Number of Travelers', 'type': 'number', 'required': False},
            ]
        }
    
    def _handle_general_info(self, message: str) -> Dict:
        """Handle general information requests"""
        # Search knowledge base
        results = self.knowledge_base.search_camps(message)
        
        if results:
            camps_data = [asdict(camp) for camp in results[:3]]
            return {
                'type': 'search_results',
                'message': f"I found {len(results)} camps that might interest you:",
                'camps': camps_data,
                'cta': 'Would you like more details about any of these?'
            }
        else:
            return {
                'type': 'general',
                'message': "Wilderness Destinations offers over 55 camps across 8 African countries, each providing unique safari and conservation experiences. I can help you find the perfect destination based on your interests. What kind of experience are you looking for? Big cats, gorilla trekking, mokoro trips, or something else?",
                'cta': 'Tell me about your dream safari!'
            }
    
    def submit_enquiry(self, enquiry_data: Dict) -> Dict:
        """Submit enquiry to Wilderness travel designers (mock API)"""
        # In production, this would call the actual API
        print(f"[MOCK API] Submitting enquiry: {json.dumps(enquiry_data, indent=2)}")
        
        return {
            'success': True,
            'message': f"Thank you, {enquiry_data.get('full_name', 'there')}! Your enquiry has been sent to our safari specialists. We'll be in touch within 24 hours to start planning your wilderness adventure. You'll also receive 24/7 support through our Wilderness24 safety logistics team once your journey begins.",
            'reference_id': f"WD-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        }


# API endpoint simulation
if __name__ == "__main__":
    chatbot = WildernessChatbot()
    
    # Test scenarios
    test_messages = [
        "I want to see big cats",
        "I'm looking for a sustainable honeymoon",
        "Tell me about gorilla trekking in Rwanda",
        "What camps do you have in Botswana?",
        "I want to sleep under the stars",
        "I'd like to speak to a specialist"
    ]
    
    print("=== Wilderness Destinations Chatbot Test ===\n")
    for msg in test_messages:
        print(f"USER: {msg}")
        response = chatbot.process_message("test_user", msg)
        print(f"BOT: {json.dumps(response, indent=2)}\n")

"""
Setswana Language Translations for Wilderness Destinations Chatbot
Provides bilingual support (English/Setswana) for the safari concierge
"""

class SetswanaTranslations:
    """Setswana language translations"""
    
    def __init__(self):
        self.translations = {
            # Greetings and Common Phrases
            'greeting': {
                'en': "Dumelang! I'm Tumi, your personal Safari Specialist at Wilderness Destinations. 🌍",
                'tn': "Dumelang! Ke Tumi, moitseanape wa gago wa Safari kwa Wilderness Destinations. 🌍"
            },
            'intro': {
                'en': "We're an award-winning conservation and hospitality company offering life-changing journeys across Africa's most iconic wild places.",
                'tn': "Re kgwebo e e tlotlegang ya tlhokomelo ya tikologo le boamogedi e e tlamelang maeto a a fetolang botshelo mo mafelong a a gakgamatsang a Afrika."
            },
            'ask_name': {
                'en': "To get started, may I have your name?",
                'tn': "Go simolola, a nka tsaya leina la gago?"
            },
            'ask_email': {
                'en': "Thank you, {name}. What is the best email address to reach you at?",
                'tn': "Ke a leboga, {name}. Aterese ya imeili e e siameng ya go ikgolaganya le wena ke efe?"
            },
            'ask_phone': {
                'en': "Perfect. And finally, what is your telephone number (including country code)?",
                'tn': "Go siame. Mme kwa bofelong, nomoro ya gago ya mogala ke efe (go akaretsa khoutu ya naga)?"
            },
            
            # Destination Introduction
            'destinations_intro': {
                'en': "Thank you, {name}! It's a pleasure to connect with you.\n\nWe offer exclusive wilderness journeys across 8 pristine African countries:",
                'tn': "Ke a leboga, {name}! Ke itumelela go ikgolaganya le wena.\n\nRe tlamela ka maeto a a kgethegileng a naga ya diphologolo mo dinageng di le 8 tsa Afrika:"
            },
            'destinations_list': {
                'en': "• Botswana 🇧🇼\n• Rwanda 🇷🇼\n• Namibia 🇳🇦\n• Kenya 🇰🇪\n• Zambia 🇿🇲\n• Zimbabwe 🇿🇼\n• Tanzania 🇹🇿\n• South Africa 🇿🇦",
                'tn': "• Botswana 🇧🇼\n• Rwanda 🇷🇼\n• Namibia 🇳🇦\n• Kenya 🇰🇪\n• Zambia 🇿🇲\n• Zimbabwe 🇿🇼\n• Tanzania 🇹🇿\n• South Africa 🇿🇦"
            },
            'ask_preference': {
                'en': "Which destination calls to you, or what kind of experience are you dreaming of?",
                'tn': "Lefelo lefe le le go bitsang, kgotsa ke boitemogelo bofe bo o bo lorang?"
            },
            
            # Experience Recommendations
            'big_cats_recommendation': {
                'en': "For exceptional big cat viewing, I recommend camps in the Okavango Delta and Rwanda's Akagera.",
                'tn': "Go bona dikatse tse dikgolo, ke akantsha dikhampo tsa Okavango Delta le Akagera kwa Rwanda."
            },
            'gorilla_recommendation': {
                'en': "For gorilla trekking, Rwanda's Bisate Lodge offers an unforgettable mountain gorilla experience.",
                'tn': "Go tsamaya o batla digorilla, Bisate Lodge kwa Rwanda e tlamela ka boitemogelo jo bo sa lebalegeng jwa digorilla tsa dithaba."
            },
            'elephant_recommendation': {
                'en': "For elephant encounters, from massive herds to rare desert-adapted elephants.",
                'tn': "Go kopana le ditlou, go tswa mo merafeng e megolo go ya kwa ditloung tsa sekaka tse di sa tlwaelegang."
            },
            'rhino_recommendation': {
                'en': "For rhino tracking experiences, Namibia and Zambia offer thrilling walking safaris.",
                'tn': "Go latela ditshukudu, Namibia le Zambia di tlamela ka maeto a a kgatlhang a go tsamaya ka dinao."
            },
            'star_beds_recommendation': {
                'en': "For sleeping under the stars, our star bed experiences in Namibia, Botswana, Zimbabwe, and Rwanda are magical.",
                'tn': "Go robala fa tlase ga dinaledi, boitemogelo jwa rona jwa dibethe tsa dinaledi kwa Namibia, Botswana, Zimbabwe le Rwanda bo a kgatlha."
            },
            'helicopter_recommendation': {
                'en': "For aerial perspectives, helicopter safaris over the Okavango Delta are breathtaking.",
                'tn': "Go bona mo godimo, maeto a helikoputara a a fofang mo godimo ga Okavango Delta a a kgatlhang."
            },
            'ballooning_recommendation': {
                'en': "For hot air ballooning, Namibia and Tanzania offer spectacular desert and savannah flights.",
                'tn': "Go fofa ka dipalune tsa moya o o bothitho, Namibia le Tanzania di tlamela ka maeto a a kgatlhang a sekaka le thaba."
            },
            'birding_recommendation': {
                'en': "For birding enthusiasts, we offer access to over 930 species across our camps.",
                'tn': "Go ba ba ratang dinonyane, re tlamela ka tsela ya go bona mefuta e e fetang 930 mo dikhampo tsa rona."
            },
            'mokoro_recommendation': {
                'en': "For traditional mokoro experiences, glide through the Okavango Delta's channels.",
                'tn': "Go itemogela mokoro wa setso, tsamaya ka bonolo mo metsweding ya Okavango Delta."
            },
            'canoeing_recommendation': {
                'en': "For canoeing adventures, paddle the iconic Zambezi River at Mana Pools.",
                'tn': "Go palama kanoe, palama Noka ya Zambezi e e itsegeng kwa Mana Pools."
            },
            
            # Countries
            'country_botswana': {
                'en': "Exploring Botswana's wilderness offerings.",
                'tn': "Go sekaseka ditlamelo tsa naga ya diphologolo ya Botswana."
            },
            'country_rwanda': {
                'en': "Exploring Rwanda's wilderness offerings.",
                'tn': "Go sekaseka ditlamelo tsa naga ya diphologolo ya Rwanda."
            },
            'country_namibia': {
                'en': "Exploring Namibia's wilderness offerings.",
                'tn': "Go sekaseka ditlamelo tsa naga ya diphologolo ya Namibia."
            },
            
            # General Information
            'general_info': {
                'en': "Wilderness Destinations offers over 55 camps across 8 African countries, each providing unique safari and conservation experiences. I can help you find the perfect destination based on your interests. What kind of experience are you looking for? Big cats, gorilla trekking, mokoro trips, or something else?",
                'tn': "Wilderness Destinations e tlamela ka dikhampo di le 55 mo dinageng di le 8 tsa Afrika, nngwe le nngwe e tlamela ka boitemogelo jo bo kgethegileng jwa safari le tlhokomelo ya tikologo. Nka go thusa go bona lefelo le le siameng go ya ka dikgatlhego tsa gago. Ke boitemogelo bofe bo o bo batlang? Dikatse tse dikgolo, go tsamaya o batla digorilla, maeto a mokoro, kgotsa sengwe?"
            },
            
            # Call to Actions
            'cta_more_info': {
                'en': "Would you like to know more about any of these camps, or shall I connect you with one of our safari specialists?",
                'tn': "A o batla go itse go feta ka ga dikhampo tseno, kgotsa a nka go golaganya le mongwe wa baitseanape ba rona ba safari?"
            },
            'cta_specialist': {
                'en': "I'd be delighted to connect you with one of our expert safari specialists! They'll help craft your perfect wilderness adventure.",
                'tn': "Ke tla itumelela go go golaganya le mongwe wa baitseanape ba rona ba safari! Ba tla go thusa go tlhama leeto la gago le le siameng la naga ya diphologolo."
            },
            'cta_dream_safari': {
                'en': "Tell me about your dream safari!",
                'tn': "Mpolelele ka safari ya gago ya ditoro!"
            },
            
            # Search Results
            'search_results': {
                'en': "I found {count} camps that might interest you:",
                'tn': "Ke bonye dikhampo di le {count} tse di ka go kgatlhang:"
            },
            'no_results': {
                'en': "Here are some of our most popular camps to get you started.",
                'tn': "Tseno ke dikhampo tse di ratiwang go go simolola."
            },
            
            # Language Switching
            'switch_to_english': {
                'en': "Switching to English",
                'tn': "Go fetogela go Seesimane"
            },
            'switch_to_setswana': {
                'en': "Switching to Setswana",
                'tn': "Go fetogela go Setswana"
            },
            'language_changed': {
                'en': "Language changed to English. How can I help you today?",
                'tn': "Puo e fetogetswe go Setswana. Nka go thusa jang gompieno?"
            },
            
            # Camp Highlights (Common Terms)
            'camp_terms': {
                'best_viewing': {'en': 'Best viewing', 'tn': 'Pono e e siameng'},
                'exclusive': {'en': 'Exclusive', 'tn': 'E e kgethegileng'},
                'year_round': {'en': 'Year-round', 'tn': 'Ngwaga otlhe'},
                'conservation': {'en': 'Conservation', 'tn': 'Tlhokomelo ya tikologo'},
                'luxury': {'en': 'Luxury', 'tn': 'Boitumelo'},
                'intimate': {'en': 'Intimate', 'tn': 'E e gaufi'},
                'remote': {'en': 'Remote', 'tn': 'E e kgakala'},
                'pristine': {'en': 'Pristine', 'tn': 'E e phepa'},
            },
            
            # Experience Names in Setswana
            'experiences': {
                'Big Cat Viewing': {'en': 'Big Cat Viewing', 'tn': 'Go Bona Dikatse Tse Dikgolo'},
                'Gorilla Trekking': {'en': 'Gorilla Trekking', 'tn': 'Go Tsamaya o Batla Digorilla'},
                'Mokoro Trips': {'en': 'Mokoro Trips', 'tn': 'Maeto a Mokoro'},
                'Game Drives': {'en': 'Game Drives', 'tn': 'Maeto a Diphologolo'},
                'Walking Safaris': {'en': 'Walking Safaris', 'tn': 'Maeto a go Tsamaya'},
                'Helicopter Safari': {'en': 'Helicopter Safari', 'tn': 'Safari ya Helikoputara'},
                'Star Beds': {'en': 'Star Beds', 'tn': 'Dibethe tsa Dinaledi'},
                'Hot Air Ballooning': {'en': 'Hot Air Ballooning', 'tn': 'Go Fofa ka Palune'},
                'Rhino Tracking': {'en': 'Rhino Tracking', 'tn': 'Go Latela Ditshukudu'},
                'Elephant Viewing': {'en': 'Elephant Viewing', 'tn': 'Go Bona Ditlou'},
                'Birding': {'en': 'Birding', 'tn': 'Go Bona Dinonyane'},
                'Canoeing': {'en': 'Canoeing', 'tn': 'Go Palama Kanoe'},
                'Fishing': {'en': 'Fishing', 'tn': 'Go Tsoma'},
                'Cultural Visits': {'en': 'Cultural Visits', 'tn': 'Maeto a Setso'},
            }
        }
    
    def get(self, key: str, lang: str = 'en', **kwargs) -> str:
        """Get translation for a key in specified language"""
        if key in self.translations:
            text = self.translations[key].get(lang, self.translations[key]['en'])
            # Format with any provided kwargs
            if kwargs:
                try:
                    return text.format(**kwargs)
                except KeyError:
                    return text
            return text
        return key
    
    def translate_experience(self, experience: str, lang: str = 'en') -> str:
        """Translate experience name"""
        if experience in self.translations['experiences']:
            return self.translations['experiences'][experience].get(lang, experience)
        return experience
    
    def translate_camp_term(self, term: str, lang: str = 'en') -> str:
        """Translate common camp terms"""
        if term in self.translations['camp_terms']:
            return self.translations['camp_terms'][term].get(lang, term)
        return term

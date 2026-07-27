#!/usr/bin/env python
# coding: utf-8

# In[17]:


import random
import string
import warnings
import nltk
from nltk.stem import WordNetLemmatizer

warnings.filterwarnings("ignore")
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")
lemmatizer = WordNetLemmatizer()


# In[9]:


intents = {

"rice_cultivation": {
    "patterns": ["rice farming", "grow rice", "paddy cultivation", "rice crop", "paddy farming"],
    "responses": [
        "Rice grows best in fertile soil with adequate water.",
        "Use certified seeds and proper irrigation for better yield.",
        "Timely fertilizer application improves rice production."
    ]
},

"wheat_cultivation": {
    "patterns": ["wheat farming", "grow wheat", "wheat cultivation", "wheat crop"],
    "responses": [
        "Wheat is mainly grown during the Rabi season.",
        "Proper irrigation and weed control improve wheat yield.",
        "Use disease-resistant wheat varieties."
    ]
},

"maize_cultivation": {
    "patterns": ["maize farming", "corn farming", "grow maize", "maize cultivation"],
    "responses": [
        "Maize requires well-drained fertile soil.",
        "Maintain proper spacing for healthy crop growth.",
        "Regular irrigation improves maize production."
    ]
},

"cotton_cultivation": {
    "patterns": ["cotton farming", "grow cotton", "cotton cultivation", "cotton crop"],
    "responses": [
        "Cotton grows well in black soil.",
        "Monitor pest attacks regularly in cotton fields.",
        "Balanced fertilization increases cotton yield."
    ]
},

"sugarcane_cultivation": {
    "patterns": ["sugarcane farming", "grow sugarcane", "sugarcane cultivation"],
    "responses": [
        "Sugarcane requires sufficient water and sunlight.",
        "Use healthy setts for planting.",
        "Proper nutrient management improves sugarcane yield."
    ]
},

"banana_farming": {
    "patterns": ["banana farming", "banana cultivation", "grow banana"],
    "responses": [
        "Banana requires fertile soil and regular irrigation.",
        "Apply organic manure for healthy growth.",
        "Protect banana plants from strong winds."
    ]
},

"mango_farming": {
    "patterns": ["mango farming", "mango cultivation", "grow mango"],
    "responses": [
        "Mango trees require good sunlight and drainage.",
        "Prune trees regularly for better fruit production.",
        "Flowering depends on seasonal conditions."
    ]
},

"tomato_farming": {
    "patterns": ["tomato farming", "grow tomato", "tomato cultivation"],
    "responses": [
        "Tomatoes require fertile soil and regular watering.",
        "Use disease-resistant tomato varieties.",
        "Support plants with stakes for better growth."
    ]
},

"potato_farming": {
    "patterns": ["potato farming", "grow potato", "potato cultivation"],
    "responses": [
        "Potatoes grow well in loose and fertile soil.",
        "Maintain adequate soil moisture.",
        "Harvest potatoes after the plants mature."
    ]
},

"chilli_farming": {
    "patterns": ["chilli farming", "grow chilli", "chili cultivation", "pepper farming"],
    "responses": [
        "Chilli requires warm weather and fertile soil.",
        "Avoid waterlogging around chilli plants.",
        "Monitor pests regularly for healthy crops."
    ]
},

"seed_treatment": {
    "patterns": ["seed treatment", "treat seeds", "seed protection"],
    "responses": [
        "Treat seeds before sowing to prevent diseases.",
        "Use recommended fungicides or bio-agents.",
        "Healthy seeds improve germination."
    ]
},

"crop_rotation": {
    "patterns": ["crop rotation", "rotate crops", "rotation farming"],
    "responses": [
        "Crop rotation improves soil fertility.",
        "Rotating crops helps reduce pests and diseases.",
        "Legumes are excellent rotational crops."
    ]
},

"intercropping": {
    "patterns": ["intercropping", "mixed cropping", "grow multiple crops"],
    "responses": [
        "Intercropping improves land utilization.",
        "It helps reduce pest infestation.",
        "Choose compatible crop combinations."
    ]
},

"mulching": {
    "patterns": ["mulching", "mulch", "cover soil"],
    "responses": [
        "Mulching conserves soil moisture.",
        "It suppresses weed growth.",
        "Organic mulch improves soil quality."
    ]
},

"rainwater_harvesting": {
    "patterns": ["rainwater harvesting", "collect rain water", "harvest rainwater"],
    "responses": [
        "Rainwater harvesting conserves water for irrigation.",
        "Stored rainwater is useful during dry seasons.",
        "It improves groundwater recharge."
    ]
},

"weather_alert": {
    "patterns": ["weather alert", "storm warning", "rain alert", "weather update"],
    "responses": [
        "Always monitor local weather alerts before farm operations.",
        "Avoid pesticide spraying during heavy rain or strong winds.",
        "Protect harvested crops from unexpected rainfall."
    ]
},

"faq": {
    "patterns": ["faq", "common questions", "frequently asked questions", "questions"],
    "responses": [
        "I can answer questions about crops, soil, irrigation, fertilizers, pests and government schemes.",
        "Ask me any agriculture-related question."
    ]
},

"working_hours": {
    "patterns": ["working hours", "office hours", "service timing", "when are you available"],
    "responses": [
        "I'm available whenever you need farming information.",
        "Agriculture department offices usually operate during regular business hours."
    ]
},

"language_support": {
    "patterns": ["languages", "language support", "can you speak tamil", "supported languages"],
    "responses": [
        "Currently I communicate in English.",
        "Future versions may support multiple regional languages."
    ]
},

"about_agriculture": {
    "patterns": ["what is agriculture", "define agriculture", "about agriculture", "agriculture meaning"],
    "responses": [
        "Agriculture is the science and practice of cultivating crops and raising livestock.",
        "Agriculture provides food, raw materials and employment to millions of people.",
        "Modern agriculture combines traditional farming with technology to improve productivity."
    ]
},

"livestock": {
    "patterns": ["livestock", "animal farming", "farm animals", "rear animals", "livestock farming"],
    "responses": [
        "Livestock farming includes cattle, goats, sheep, pigs and poultry.",
        "Healthy livestock management improves farm income.",
        "Proper nutrition and vaccination are essential for livestock."
    ]
},

"dairy_farming": {
    "patterns": ["dairy farming", "milk production", "cow farming", "buffalo farming", "dairy"],
    "responses": [
        "Dairy farming requires quality feed, clean water and regular healthcare.",
        "Healthy cattle produce better quality milk.",
        "Maintain proper hygiene in dairy farms."
    ]
},

"poultry_farming": {
    "patterns": ["poultry farming", "chicken farming", "broiler", "layer farming", "poultry"],
    "responses": [
        "Poultry farming can produce meat and eggs.",
        "Maintain proper ventilation and vaccination schedules.",
        "Clean housing reduces disease outbreaks."
    ]
},

"goat_farming": {
    "patterns": ["goat farming", "goat rearing", "raise goats", "goat business"],
    "responses": [
        "Goat farming is profitable with proper feeding and healthcare.",
        "Choose healthy breeds for better productivity.",
        "Provide clean shelter and fresh drinking water."
    ]
},

"sheep_farming": {
    "patterns": ["sheep farming", "sheep rearing", "raise sheep", "wool farming"],
    "responses": [
        "Sheep farming is useful for wool and meat production.",
        "Healthy grazing land improves sheep growth.",
        "Regular deworming keeps sheep healthy."
    ]
},

"fish_farming": {
    "patterns": ["fish farming", "aquaculture", "fish culture", "fish pond", "rear fish"],
    "responses": [
        "Fish farming requires clean water and quality fish feed.",
        "Maintain proper oxygen levels in ponds.",
        "Healthy water quality improves fish production."
    ]
},

"bee_keeping": {
    "patterns": ["beekeeping", "bee farming", "honey farming", "apiary", "honey bees"],
    "responses": [
        "Beekeeping provides honey and improves crop pollination.",
        "Protect bee colonies from pesticides.",
        "Healthy bee colonies increase honey production."
    ]
},

"farm_equipment": {
    "patterns": ["farm equipment", "agriculture tools", "farm tools", "equipment", "implements"],
    "responses": [
        "Modern farm equipment reduces labor and saves time.",
        "Maintain farm tools regularly for better performance.",
        "Choose equipment suitable for your farm size."
    ]
},

"tractor": {
    "patterns": ["tractor", "buy tractor", "tractor types", "tractor maintenance"],
    "responses": [
        "Choose a tractor based on your land size and farming needs.",
        "Regular servicing increases tractor life.",
        "Proper maintenance reduces repair costs."
    ]
},

"machinery_rental": {
    "patterns": ["rent machinery", "tractor rental", "equipment rental", "hire machinery"],
    "responses": [
        "Machinery rental is a cost-effective option for small farmers.",
        "Many government centers provide machinery on rent.",
        "Renting equipment reduces investment costs."
    ]
},

"drone_farming": {
    "patterns": ["drone farming", "agriculture drone", "spray drone", "farm drone"],
    "responses": [
        "Agricultural drones help monitor crops and spray pesticides.",
        "Drone technology saves time and labor.",
        "Drones improve precision farming practices."
    ]
},

"smart_farming": {
    "patterns": ["smart farming", "digital farming", "modern farming", "technology in farming"],
    "responses": [
        "Smart farming uses sensors, GPS and automation.",
        "Technology helps improve productivity and reduce costs.",
        "Modern farming increases efficiency."
    ]
},

"precision_farming": {
    "patterns": ["precision farming", "precision agriculture", "site specific farming"],
    "responses": [
        "Precision farming applies inputs only where needed.",
        "GPS and sensors improve farming accuracy.",
        "It helps reduce waste and increase yield."
    ]
},

"iot_agriculture": {
    "patterns": ["iot in agriculture", "smart sensors", "farm sensors", "iot farming"],
    "responses": [
        "IoT sensors monitor soil moisture, weather and crop health.",
        "Smart sensors help farmers make better decisions.",
        "IoT improves resource management."
    ]
},

"soil_health": {
    "patterns": ["soil health", "healthy soil", "improve soil", "soil fertility"],
    "responses": [
        "Healthy soil improves crop productivity.",
        "Organic matter and crop rotation improve soil fertility.",
        "Regular soil testing helps maintain soil health."
    ]
},

"export_information": {
    "patterns": ["export crops", "crop export", "export agriculture", "international market"],
    "responses": [
        "Export quality crops require proper grading and packaging.",
        "Follow export regulations before shipping products.",
        "High-quality produce has better export opportunities."
    ]
},

"cold_storage": {
    "patterns": ["cold storage", "store vegetables", "fruit storage", "cold warehouse"],
    "responses": [
        "Cold storage extends the shelf life of fruits and vegetables.",
        "Proper temperature control reduces spoilage.",
        "Cold storage improves product quality."
    ]
},

"subsidies": {
    "patterns": ["farmer subsidy", "government subsidy", "agriculture subsidy", "equipment subsidy"],
    "responses": [
        "Government subsidies are available for irrigation, machinery and seeds.",
        "Visit your agriculture office for subsidy details.",
        "Eligibility depends on the scheme and region."
    ]
},

"contact_support": {
    "patterns": ["contact", "customer support", "help desk", "support number", "contact advisor"],
    "responses": [
        "Please contact your nearest Agriculture Extension Office for further assistance.",
        "Your local agriculture department can provide expert guidance.",
        "You can also consult certified agricultural officers."
    ]
},

"feedback": {
    "patterns": ["feedback", "give feedback", "suggestion", "report problem", "complaint"],
    "responses": [
        "Thank you for your feedback. It helps improve the chatbot.",
        "Your suggestions are valuable to us.",
        "We appreciate your comments."
    ]
},

"crop_insurance": {
    "patterns": ["crop insurance", "insurance for crops", "pmfby", "protect my crops", "insurance scheme"],
    "responses": [
        "Crop insurance helps farmers reduce losses caused by natural disasters.",
        "You can enroll in crop insurance through authorized agencies.",
        "Crop insurance provides financial protection against crop failure."
    ]
},

"loan_information": {
    "patterns": ["agriculture loan", "farmer loan", "crop loan", "loan for farming", "bank loan"],
    "responses": [
        "Many banks provide agricultural loans with attractive interest rates.",
        "Visit your nearest bank to learn about farmer loan eligibility.",
        "Agricultural loans can help purchase seeds, fertilizers, and machinery."
    ]
},

"market_price": {
    "patterns": ["market price", "crop price", "mandi price", "selling price", "market rate"],
    "responses": [
        "Crop prices change daily based on market demand.",
        "Check your nearest mandi for today's crop prices.",
        "Selling at the right time helps maximize profit."
    ]
},

"storage": {
    "patterns": ["crop storage", "grain storage", "store crops", "warehouse", "storage methods"],
    "responses": [
        "Store harvested crops in clean and dry warehouses.",
        "Proper storage reduces spoilage and pest attacks.",
        "Use moisture-free storage for longer shelf life."
    ]
},

"harvesting": {
    "patterns": ["harvesting", "when to harvest", "crop harvest", "harvest time", "harvesting methods"],
    "responses": [
        "Harvest crops only after they reach full maturity.",
        "Proper harvesting techniques reduce crop losses.",
        "Harvest timing varies depending on the crop."
    ]
},

"compost": {
    "patterns": ["compost", "make compost", "organic compost", "compost preparation", "compost fertilizer"],
    "responses": [
        "Compost improves soil fertility naturally.",
        "Organic compost is made from plant and animal waste.",
        "Regular compost application improves soil health."
    ]
},

"vermicompost": {
    "patterns": ["vermicompost", "earthworm compost", "worm compost", "vermi fertilizer"],
    "responses": [
        "Vermicompost is produced using earthworms.",
        "It provides essential nutrients for healthy plant growth.",
        "Vermicompost improves soil structure and fertility."
    ]
},

"drip_irrigation": {
    "patterns": ["drip irrigation", "drip system", "drip watering", "drip method"],
    "responses": [
        "Drip irrigation delivers water directly to plant roots.",
        "It saves water and increases irrigation efficiency.",
        "Drip irrigation is ideal for fruit and vegetable crops."
    ]
},

"sprinkler_irrigation": {
    "patterns": ["sprinkler irrigation", "sprinkler system", "sprinkler method"],
    "responses": [
        "Sprinkler irrigation distributes water like rainfall.",
        "It is suitable for many field crops.",
        "Sprinklers provide uniform water distribution."
    ]
},

"greenhouse_farming": {
    "patterns": ["greenhouse farming", "polyhouse", "green house", "protected cultivation"],
    "responses": [
        "Greenhouse farming protects crops from harsh weather.",
        "It allows year-round cultivation of vegetables and flowers.",
        "Controlled environments improve crop quality."
    ]
},

"hydroponics": {
    "patterns": ["hydroponics", "soil less farming", "hydroponic farming", "grow without soil"],
    "responses": [
        "Hydroponics grows plants without soil using nutrient-rich water.",
        "It requires less water than traditional farming.",
        "Hydroponics is popular for leafy vegetables."
    ]
},

"fruit_farming": {
    "patterns": ["fruit farming", "grow fruits", "orchard", "fruit cultivation"],
    "responses": [
        "Fruit farming requires proper irrigation and nutrient management.",
        "Common fruit crops include mango, banana, and guava.",
        "Healthy orchards produce better-quality fruits."
    ]
},

"vegetable_farming": {
    "patterns": ["vegetable farming", "grow vegetables", "vegetable cultivation"],
    "responses": [
        "Vegetables require fertile soil and regular watering.",
        "Tomato, brinjal, and chili are widely cultivated vegetables.",
        "Use quality seeds for better vegetable production."
    ]
},

"flower_farming": {
    "patterns": ["flower farming", "grow flowers", "floriculture", "flower cultivation"],
    "responses": [
        "Floriculture is the cultivation of flowering plants.",
        "Marigold, rose, and jasmine are popular flower crops.",
        "Proper sunlight and irrigation improve flower quality."
    ]
},

"medicinal_plants": {
    "patterns": ["medicinal plants", "herbal plants", "medicinal farming", "grow herbs"],
    "responses": [
        "Medicinal plants have high commercial value.",
        "Tulsi, Aloe Vera, and Ashwagandha are commonly grown medicinal plants.",
        "Demand for herbal products is increasing."
    ]
},

"weed_control": {
    "patterns": ["weed control", "remove weeds", "weed management", "control weeds"],
    "responses": [
        "Weeds compete with crops for nutrients and water.",
        "Regular weeding improves crop growth.",
        "Mechanical and chemical methods can control weeds."
    ]
},

"plant_nutrition": {
    "patterns": ["plant nutrients", "crop nutrients", "plant nutrition", "nutrient deficiency"],
    "responses": [
        "Plants require nitrogen, phosphorus, and potassium for healthy growth.",
        "Micronutrients are also essential for crop development.",
        "Balanced nutrition improves crop yield."
    ]
},

"climate_change": {
    "patterns": ["climate change", "global warming", "weather changes", "climate effects"],
    "responses": [
        "Climate change affects rainfall and crop productivity.",
        "Sustainable farming helps reduce climate impacts.",
        "Choosing climate-resilient crops can reduce risk."
    ]
},

"farm_safety": {
    "patterns": ["farm safety", "safety in farming", "farmer safety", "safe farming"],
    "responses": [
        "Wear protective equipment while spraying pesticides.",
        "Handle machinery carefully to avoid accidents.",
        "Always follow safety guidelines during farm work."
    ]
},

"first_aid": {
    "patterns": ["first aid", "farm injury", "emergency help", "accident in farm"],
    "responses": [
        "Provide immediate first aid and seek medical assistance if necessary.",
        "Keep a first aid kit available on the farm.",
        "Treat injuries promptly to prevent complications."
    ]
},

"greeting": {
    "patterns": ["hi", "hello", "hey", "good morning", "good evening", "howdy", "hi there", "hello bot"],
    "responses": [
        "Hello! Welcome to AgroBot. How can I help you today?",
        "Hi! I'm your Agriculture Advisor.",
        "Greetings! Ask me anything about farming."
    ]
},

"goodbye": {
    "patterns": ["bye", "goodbye", "see you", "exit", "quit", "stop", "close chatbot"],
    "responses": [
        "Goodbye! Wishing you a successful harvest.",
        "See you again. Happy Farming!",
        "Take care and have a productive day."
    ]
},

"thanks": {
    "patterns": ["thanks", "thank you", "thanks a lot", "appreciate it", "thank you so much"],
    "responses": [
        "You're welcome!",
        "Happy to help.",
        "Glad I could assist you."
    ]
},

"bot_name": {
    "patterns": ["what is your name", "who are you", "your name", "introduce yourself"],
    "responses": [
        "I'm AgroBot, your Agriculture Advisor.",
        "You can call me AgroBot.",
        "I'm here to help farmers with agricultural information."
    ]
},

"creator": {
    "patterns": ["who created you", "who made you", "your developer", "who built you"],
    "responses": [
        "I was developed as an Agriculture Advisor chatbot.",
        "A Python developer created me to assist farmers."
    ]
},

"help": {
    "patterns": ["help", "what can you do", "services", "menu", "available options"],
    "responses": [
        "I can help with crops, fertilizers, irrigation, pests, diseases, government schemes and more.",
        "Ask me anything related to agriculture."
    ]
},

"crop_recommendation": {
    "patterns": ["recommend crop", "best crop", "which crop should i grow", "crop suggestion", "suggest crop"],
    "responses": [
        "Crop selection depends on soil type, climate and season.",
        "Tell me your soil type for better recommendations.",
        "Rice, wheat, maize and millets are popular depending on your region."
    ]
},

"seasonal_crops": {
    "patterns": ["seasonal crops", "kharif crops", "rabi crops", "zaid crops", "crop season"],
    "responses": [
        "Kharif crops include rice and maize.",
        "Rabi crops include wheat and mustard.",
        "Season selection is important for better yield."
    ]
},

"soil_type": {
    "patterns": ["soil type", "types of soil", "black soil", "red soil", "alluvial soil", "clay soil", "sandy soil"],
    "responses": [
        "Common soil types are black, red, sandy, clay and alluvial soil.",
        "Different crops perform better in different soils."
    ]
},

"soil_testing": {
    "patterns": ["soil testing", "test soil", "soil nutrients", "soil health card"],
    "responses": [
        "Soil testing helps determine nutrient deficiencies.",
        "Testing soil before sowing improves productivity."
    ]
},

"fertilizer_info": {
    "patterns": ["fertilizer", "best fertilizer", "urea", "dap", "npk fertilizer", "organic fertilizer"],
    "responses": [
        "Choose fertilizers based on soil test reports.",
        "Balanced NPK and organic compost improve crop growth.",
        "Avoid overusing chemical fertilizers."
    ]
},

"organic_farming": {
    "patterns": ["organic farming", "natural farming", "chemical free farming", "organic agriculture"],
    "responses": [
        "Organic farming uses natural fertilizers and pest control.",
        "Compost and vermicompost are widely used in organic farming."
    ]
},

"irrigation": {
    "patterns": ["irrigation", "watering", "drip irrigation", "sprinkler irrigation", "water crops"],
    "responses": [
        "Drip irrigation saves water and increases efficiency.",
        "Proper irrigation depends on crop and soil type."
    ]
},

"water_management": {
    "patterns": ["save water", "water management", "water conservation", "rain water harvesting"],
    "responses": [
        "Rainwater harvesting helps conserve water.",
        "Use drip irrigation to reduce water wastage."
    ]
},

"pest_control": {
    "patterns": ["pest control", "crop pests", "remove insects", "control pests", "insects in crops"],
    "responses": [
        "Integrated Pest Management is recommended.",
        "Use approved pesticides only when necessary."
    ]
},

"crop_disease": {
    "patterns": ["crop disease", "plant disease", "leaf disease", "yellow leaves", "fungus"],
    "responses": [
        "Disease depends on crop and symptoms.",
        "Remove infected plants and consult experts if needed."
    ]
},

"seed_selection": {
    "patterns": ["best seeds", "seed selection", "quality seeds", "hybrid seeds"],
    "responses": [
        "Always choose certified quality seeds.",
        "Healthy seeds improve germination and yield."
    ]
},

"weather": {
    "patterns": ["weather", "rain", "temperature", "climate", "weather forecast"],
    "responses": [
        "Weather plays an important role in farming.",
        "Check the forecast before irrigation or spraying pesticides."
    ]
},

"government_schemes": {
    "patterns": ["government schemes", "farmer schemes", "pm kisan", "agriculture schemes", "subsidies"],
    "responses": [
        "Many government schemes provide financial support to farmers.",
        "Visit your nearest agriculture office for the latest scheme information."
    ]
},

"fallback": {
    "patterns": [],
    "responses": [
        "Sorry, I didn't understand your question.",
        "Could you please rephrase your question?",
        "I'm still learning. Please ask another agriculture-related question."
    ]
}

}


# In[10]:


def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens


# In[11]:


# Preprocessing
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens


# In[12]:


# Prepare Patterns
processed_patterns = {
    tag: [preprocess(pattern) for pattern in data["patterns"]]
    for tag, data in intents.items()}


# In[13]:


# Intent Matching
def score_intent(user_tokens, pattern_tokens):
    if not pattern_tokens:
        return 0
    overlap = len(set(user_tokens) & set(pattern_tokens))
    return overlap / len(set(pattern_tokens))

def match_intent(user_text, threshold=0.8):
    user_tokens = preprocess(user_text)
    best_tag = "fallback"
    best_score = 0
    for tag, patterns in processed_patterns.items():
        if tag == "fallback":
            continue
        for pattern in patterns:
            score = score_intent(user_tokens, pattern)
            if score > best_score:
                best_score = score
                best_tag = tag
    if best_score < threshold:
        return "fallback"
    return best_tag

def get_response(user_text):
    tag = match_intent(user_text)
    return random.choice(intents[tag]["responses"])


# In[15]:


# Chatbot
def run_chatbot():
    print('---------TEXT CHATBOT-------------')
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You : ")
        response = get_response(user)
        print("Bot :", response)
        if match_intent(user) == "goodbye":
            break
run_chatbot()


# In[ ]:





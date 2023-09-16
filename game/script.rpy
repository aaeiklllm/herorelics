

define m = Character("Maria Orosa")
define c = Character("Clerk")
define s = Character("Sixto")
define p = Character("Paramedic")
define j = Character("Juliana")
define a = Character("Apprentice")
define v = Character("Vicente")
define h = Character("Helen")
define p = Character("Paramedic")



transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.5 xmaximum 300 at alpha_dissolve

init:
    $ timer_range = 0
    $ timer_jump = 0


label start:
label chapter_1:
    $ lastsave = "chapter_1"
    play music "audio/prologue.mp3"

    scene chapcard1
    with fade
    pause

    scene bg1taal
    with fade
    "My hometown Taal in Batangas is such a beautiful place."

    scene bg1grassland

    "I love frolicking in its fields,"

    scene bg1beach

    "Playing with my friends and family at the beaches' white sand,"

    scene bg1ricefield

    "And helping the farmers during harvest time."

    scene bg1taalaerial

    "I was born here on the 29th of November 1893 in Taal, Batangas, fourth to be born among seven of my siblings."

    scene juliana_frame

    "My father, Simplicio A. Orosa died when I was very young so my mother Juliana L. Ylanan-Orosa worked hard everyday to provide for me and my siblings."

    scene bg1revwar
    with fade
    "Life was not easy because of the revolution which started three years after I was born."

    scene bg1phamwar
    with fade
    "Three more years later, the Philippine-American War began."

    play music "audio/everest.mp3"

    scene bg1livingroom
    with fade

    show ch1jfrown
    with dissolve
    j "*sigh*"

    hide ch1jfrown
    show ch1_mariaworried
    with dissolve
    m "\"Mother, is something wrong?\""

    hide ch1_mariaworried
    show ch1jworried
    with dissolve
    j "\"I just read the newspaper, it looks like there is war happening\""

    hide ch1jworried
    show ch1_mariacurious
    with dissolve
    m "\"What happens in a war, mother?\""

    hide ch1_mariacurious
    show ch1jtired
    with dissolve
    j "\"My dear, you are too young to understand this but, but it is a very bad event, many people get hurt and families starve.\""

    hide ch1jtired
    show ch1_mariaworried
    with dissolve
    "{i}As I listened to my mother’s description, I felt my mouth curve to a frown. Why would people want something so terrible to happen?"

    hide ch1_mariaworried
    show ch1jfrown
    with dissolve
    j "\"Maria you look sad\""

    hide ch1jfrown
    show ch1_mariapray
    with dissolve
    m "\"I can’t help but imagine those poor people suffering, mother. You always brought our family food. I want people to have something to eat everyday too.\""

    hide ch1_mariapray
    show ch1_mariasidefrown
    with dissolve
    "{i}Although I can see the surprise in my mother’s expression, I did not sense any anger. I’m glad I did not say anything unpleasant. She lifted her hand to caress my cheeks."

    hide ch1_mariasidefrown
    show ch1jsmile2
    with dissolve
    j "\"I do too, that is why we must keep our stores open for anyone who needs something to eat. Is that clear?\""


    hide ch1jsmile2
    show ch1_mariaclosedsmile
    with dissolve
    m "\"Yes, mother.\""

    scene juliana_simplicio1
    with fade
    "My father was one of the people who fought for independence. He acquired a role in the Philippine Commission which made life comfortable for my family."

    "When he died at the young age of 45, my mother struggled to make ends meet. Me and my siblings did everything we could to lessen the weight on her shoulders. As a family, we managed to pull through."

label c1s2:
    scene bg1bedroomwindow
    with fade
    show ch1s2_mariasando
    with dissolve
    "Hearing the roosters’ call, I opened my eyes to see the morning light seeping through the window. I get up to…"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'gameover'
    show screen countdown
    play music "audio/decision.mp3"
    menu:
        "What should I do?"
        "Leave the house and hang out with my friends on the street.":
            hide screen countdown
            jump c1s2r1
        "Prepare myself to help out at the general store.":
            hide screen countdown
            jump c1s2r2
    return

label gameover:

    "Game Over"

    menu:
        "Main menu":
            "ree"
            return
        "Go back to previous decision":
            $ renpy.jump("".join([lastsave]))

label c1s2r1:
    play music "audio/maman.mp3"
    scene bg1kidsplay
    with fade
    show ch1s2_mariawrong1
    with dissolve
    "I had plenty of fun hanging out with my friends. We played tag, charades, and rode carabaos at Marina’s farm."

    scene bg1kidshome
    with fade
    "It was starting to get dark so I said goodbye to my friends and headed straight home."

    scene bg1livingroomdoor
    with fade
    "Once I arrived back, I opened the door to my home."

    show ch1s2_mariawrong2
    with dissolve
    stop music
    m "\"I’m home! Where is everybo--\""

    hide ch1s2_mariawrong2
    show ch1s2_mariawrong4
    with dissolve
    pause
    scene juliana_sick2
    play music "audio/anxious.mp3"
    "...I then stopped when I saw my mother unconscious on our couch, my siblings surrounding her with worried faces."
    "I immediately went to join them, holding my mother’s hand."
    "I turned to my elder brother Vicente for an explanation."

    show ch1s2_mariawrong3
    with dissolve
    m "\"Brother, what happened?\""

    hide ch1s2_mariawrong3
    show ch1s2_vicente
    with dissolve
    v "\"Mother had collapsed. We think she overworked herself today.\""

    hide ch1s2_vicente
    show ch1s2_sixto
    with dissolve
    s "\"I wish I put off the errands I had outside. If I had stayed and helped our mother, she wouldn’t have ended up like this.\""

    hide ch1s2_sixto
    show ch1s2_vicente
    with dissolve
    v "\"Don’t worry, brother. I sent the others to go ask our neighbors for help. We’re taking her to the hospital so we can understand what’s going on.\""

    scene black
    with fade
    "That night, we were told by the doctor that my mother had been working hard to the point of exhaustion. She had become sickly and was advised to rest in the hospital for days until she got her strength back."

    "Her fees, medication, and supplements caused a huge dent on our family’s savings. Since then, we got into a nearly endless cycle of borrowing money and paying debt."

    "Because of selfish decisions, including mine, our life took a turn for the worst. As the war wages, I see no silver lining in our current circumstance."

    jump gameover

label c1s2r2:
    play music "audio/plusheen.mp3"
    scene bg1bedroomwindow
    with fade
    "After washing my face and brushing my teeth, I proceeded to get dressed."

    "I tied my hair back neatly in a bun, and tucked my shirt under my skirt."

    scene bg1hallway
    with fade
    "I walked down the hallway and opened the door leading to our store with a smile on my face."
    scene bg1opendoor
    with dissolve

    scene bg1store
    with fade

    show ch1s2_mariacorrect2
    with dissolve
    m "\"Good morning!\""

    hide ch1s2_mariacorrect2
    show ch1jsmile1
    with dissolve
    j "\"Oh, good morning, dear. What brings my Maria here?\""

    hide ch1jsmile1
    show ch1s2_mariacorrect3
    with dissolve
    m "\"I’m here to help you tend to customers, of course.\""

    hide ch1s2_mariacorrect3
    show ch1jsmile2
    with dissolve
    j "\"Don’t you have exams to study for? Perhaps you can spend time with your friends today.\""

    hide ch1jsmile2
    show ch1s2_mariacorrect4
    with dissolve
    m "\"I’ve done everything I need for school, and I get to hang out with Marina and the others at the campus too. You look tired, mother. Please rest for a while, I’ll handle the store.\""

    hide ch1s2_mariacorrect4
    show ch1jthankful
    with dissolve
    j "\"I am feeling a bit tired. Alright then, Ms. Responsible. I’ll be in the living room, don’t hesitate to ask for assistance when you’re unsure.\""

    hide ch1jthankful
    show ch1s2_mariacorrect1
    with dissolve
    "With a chuckle, my mother leaves the room. She had been working tirelessly to keep our family healthy and well cared for. This is the least that my siblings and I could do to give her ease."

    "Since that day, my siblings and I have unanimously decided to help our mother. Be it household chores such as cleaning, or keeping our business up and running, we took turns so that mother will have to do the least amount of work possible."

    scene black
    with fade
    "After some years, my older siblings graduated one by one. Meanwhile, I worked hard and got accepted at one of the finest universities in the country."

    jump chapter_2

    label chapter_2:
    play music "audio/chill.mp3"
    $ lastsave = "chapter_2"

    scene chapcard2
    with fade
    pause

    scene bgaerial
    with fade
    "By the time I grew up, I had spent my elementary and high school studies in my province of Taal, Batangas."

    scene bg2up
    with fade
    "In 1915, I took up a pharmacy course at the University of the Philippines Manila."

    scene bg2seattle
    with fade
    "In 1916, some US government officials recognized my talents while I'm still studying at the University of the Philippines."

    "They sent me to Seattle to study pharmaceutical chemistry as a partial government scholar."

    "I, however, worked a series of odd jobs to pay for my tuition."

    scene bg2room
    with fade
    show ch2s1_maria1
    with dissolve

    m "\"It is summer break again. I have a lot of free time to work for the whole duration, but I guess I have to do something I may have experience with.\""

    "{i} I grab the newspaper sitting neatly on top of my desk."

    hide ch2s1_maria1
    show ch2s1_maria6
    with dissolve
    m "\"It seems there is an opening for a salmon cannery, and another one as an assistant for a local bookstore. Which of these jobs can prove my experience to be helpful?\""

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'gameover'
    show screen countdown
    play music "audio/decision.mp3"
    menu:
        "What should I do?"
        "Reach out to the salmon cannery to apply as a worker.":
            hide screen countdown
            jump c2s1r1
        "Contact the local bookstore to apply for a job there.":
            hide screen countdown
            jump c2s1r2
    return

label c2s1r2:
    scene bg2room
    with fade
    show ch2s1_maria4
    with dissolve
    play music "audio/chill.mp3"
    m "\"Local bookstore it is. I just have to find the address. I guess I'll read books for the whole summer break.\""

    scene bg2bookstore
    with fade
    "My time at the bookstore was rather… interesting."

    "Well, not really."

    "I have spent most of my shift just reading."

    "There were not many customers to tend to on a daily basis."

    "I guess the owner realized this when he decided to pay me half the wage we agreed on."

    "I feel like I have wasted my time."

    "I should’ve worked somewhere else."

    jump gameover

label c2s1r1:
    play music "audio/retro.mp3"
    scene bg2room
    with fade
    show ch2s1_maria5
    m "\"I think I’ll try something new this time. I’ve never worked at a canning factory before. This will really contribute to my knowledge and my experience when it comes to food chemistry.\""

    scene bgsalmon
    with fade
    hide ch2s1_maria5
    "I have spent my summer break working at the salmon cannery, learning about industrial preservation and packaging methods which may prove helpful in the future."

    "During my time as a factory worker, I learned more about the nutrients in fish."

    "Considering the fact that my home country is an archipelago, we can thrive in the field of fishery to boost our economy and support the livelihood of Filipinos."

    scene bg2up
    with fade
    "I earned my Bachelor of Science in Pharmaceutical Chemistry in 1917, a bachelor's degree in Food Chemistry in 1918, a degree in Pharmacy in 1920, and a master's degree in Pharmacy in 1921."
    "I worked as an assistant to Dean Charles Johnson of Washington University to support my studies."

    scene black
    with fade
    "Still, my path was not easy. I faced significant gender and racial barriers. I wrote glimpses of my hardships in my letters to home."
jump chapter_3

label chapter_3:
    $ lastsave = "chapter_3"
    play music "audio/scifi.mp3"

    scene chapcard3
    with fade
    pause

    scene i1
    with fade

    "I returned to the Philippines in 1922 and after a brief teaching stint at Centro Escolar University."

    "Entered the Bureau of Sciences, where I applied my scientific knowledge to the problems of malnutrition and food insecurity."

    "To improve the use and conservation of domestic foods, I experimented with preservation techniques such as canning, dehydrating, fermenting, and freezing local produce and protein sources."

    scene i2
    with fade

    "Along with boosting the food supply, I would like to introduce new flavors and economic opportunities."

    show ia3
    with dissolve

    "I turn to face my apprentice who wants to help her small village."

    "I am hopeful that she and the others will relay the information I’m giving her to the people of these communities."

    "I would like to see the Philippines being self-sustained and independent."

    hide ia3
    show ia2
    with dissolve
    a "\"That would be very useful, ma’am.\""

    hide ia2
    show ia4
    with dissolve
    a "\"The war has pushed the people to hold on to scarce resources.\""

    hide ia4
    show ia2
    with dissolve
    a "\"We must think of ways to prolong the rations.\""

    hide ia2
    show im1
    with dissolve
    m "\"You’re right.\""

    hide im1
    show im5
    with dissolve
    m "\"I’d like to ask you a series of questions.\""

    hide im5
    show im3
    with dissolve
    m "\"First, what do you think is best to do to enable the exportation of mangoes across the globe?\""

    hide im3
    show ia2
    with dissolve
    a "\"Since mangoes contain natural sugars, maybe we can try adding more so it will act as a preservative?\""

    hide ia2
    show im5
    with dissolve
    m "\"Hmm, that is possible.\""

    hide im5
    show im6
    with dissolve
    m "\"However, too much sweetness is not a very pleasant taste for most people.\""

    hide im6
    show im2
    with dissolve

    m "\"Too much sugar will lead to certain diseases such as throat inflammation and diabetes.\""

    hide im2
    show ia2
    with dissolve
    a "\"I see.\""

    hide ia2
    show ia4
    with dissolve
    a "\"Then, would freezing and canning be more suitable?\""

    hide ia4
    show im4
    with dissolve

    m "\"Yes, it would.\""

    hide im4
    show im5
    with dissolve

    m "\"We can try lowering the temperature and canning the mangoes to inhibit microorganism growth.\""

    hide im5
    show im2
    with dissolve

    m "\"Canned fruit is also a popular choice overseas.\""

    hide im2
    show im6
    with dissolve

    m "\"You just have to submerge the mango slices in a solution that will preserve it without altering too much of the flavor.\""
    hide im6
    with dissolve

    "This is just one example of the busy days I have working in the laboratory, with the people, and in my own home."

    "I have studied and promoted the use of indigenous ingredients, the culinary potential of which had been sidelined and scorned through centuries of colonialism."

    show flour
    with dissolve
    "I was able to produce flour"

    hide flour
    show coconuts
    with dissolve
    "from cassava, green bananas, and coconuts."

    hide coconuts
    show wine
    with dissolve
    "I fermented wine using native fruits and nuts,"

    hide wine
    show vinegar
    with dissolve
    "coaxed vinegar from pineapples,"

    hide vinegar
    show agar
    with dissolve
    "and transformed seaweed into agar."

    hide agar
    scene i3
    with fade

    "When I got home from work, I thought about the food I ate in Seattle, the condiments to be specific."

    "Ketchup and mayonnaise were top picks for the Americans."

    "They do enhance the taste of various dishes and can be used for cooking too."

    "However, I would like to make tomato ketchup more available to the Filipinos."

    show im5
    with dissolve

    m "\"Could there be a way to make ketchup without tomatoes as the main ingredient?\""

    hide im5
    with dissolve

    scene i4
    with fade

    show bananas
    with dissolve
    "I looked around my kitchen and my eyes caught the bright yellow bananas sitting on top of my dining table."

    "Come to think of it, the Philippines is a tropical country after all."

    "We have plenty of banana trees in the provinces."

    "They cost cheaper than tomatoes too."

    hide bananas
    show im5
    with dissolve

    m "\"But bananas are sweet and tomatoes are rather sour.\""

    m "\"How can I make this more savory?\""

    hide im5
    show im1
    with dissolve

    m "\"I'll never know if i never try.\""

    hide im1
    with dissolve

    show brownsugar
    with dissolve
    "{i}I picked up the jar of brown sugar from my counter, got the vinegar from the cupboard, and a few spices to add to the mix."

    hide brownsugar
    show im3
    with dissolve
    m "\"The vinegar and brown sugar will work in harmony with each other.\""

    hide im3
    show im5
    with dissolve

    m "\"The acids from the vinegar will be neutralized.\""

    hide im5
    show im3
    with dissolve

    m "\"Spices such as salt and pepper will add more kick to the taste.\""

    hide im3
    show im7
    with dissolve

    m "\"Am I missing something?\""

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'gameover'
    show screen countdown
    play music "audio/decision.mp3"
    menu:
        "What should I do?"
        "Add cornstarch to the recipe":
            hide screen countdown
            jump Hey
        "No, it's complete":
            hide screen countdown
            jump Hoy

            return

    label Hey:
        play music "audio/spongebob.mp3"
        hide im5
        show im7
        with dissolve
        m "\"Oh no!\""

        hide im7
        show cornstarch
        with dissolve

        "After adding cornstarch to the mixture, it became as thick as dough."

        hide cornstarch
        with dissolve

        "Crushed bananas are already thick so there’s no need to add cornstarch to make the consistency thicker."

        show im3
        with dissolve

        "I should have guessed that."

        hide im3
        show im7
        with dissolve

        "What am I going to do with this clump of banana dough? What a waste at a time of scarcity."
    jump gameover

    label Hoy:
        play music "audio/cook.mp3"
        hide im7
        show im4
        with dissolve
        m "\"All done!\""

        m "\"The banana ketchup recipe was a success!\""

        hide im4
        show im3
        with dissolve

        m "\"The golden mixture gave the same effect as ketchup, but it is milder due to its sweetness.\""

        scene black
        with fade

        "I gave the recipe to the communities around my place."

        "This will be very useful for carenderias too."

        "Instead of the more expensive tomato sauce, they can use this as a substitute for cooking."

        scene i2

        play music "audio/inspire.mp3"

        "A few days later, I am back at usual duties."

        "I decided to have lunch with my apprentice who, for some reason, had tried making the banana ketchup recipe."

        show chicken
        with dissolve
        "She had brought fried chicken and tomato slices to the table."

        hide chicken
        show ic1
        with dissolve
        a "\"Ma’am! This is delicious.\""

        a "\"Everyone in my village loves the banana ketchup recipe you made!\""
        hide ic1
        show ic2
        with dissolve
        "Thankfully, the recipe is well-received."

        "I’ll continue to make more innovations for the sake of my community and country."
        hide ic2
        with dissolve

        scene black
        with fade

        "At a time where few women scientists were recognized for their contributions, the Philippine government supported and funded my research."
        "In 1927, the Legislature created the Division of Food Preservation and promoted me to its Head."
        "The following year, I traveled around the world on government funding to study innovations in processing and packaging techniques."
        "I then adapted these modern foreign techniques to fit the context and culture of the Philippines"
jump chapter_4

label chapter_4:
    $ lastsave = "chapter_4"
    play music "audio/dramatic.mp3"

    scene chapcard4
    with fade
    pause

    scene bgeyes
    with fade

    "To describe the place...everywhere is bleak."

    "The sun might have stopped rising."

    "It does not show up for years of being covered with smoke from relentless firing of firearms."

    "The bombs are exploding from unknown places."

    "The cries of wounded Filipino soldiers make the whole scene bleaker than before."

    "Their bodies might look spiritless, but in their eyes, one can sense the rigorousness of being to fight for their country."

    scene bgkitchen
    with fade
    play music "audio/lofi.mp3"

    "I see Helen from the other side of the room, and she is walking towards me."

    show helencry
    with dissolve

    h "\"Kapitana! I am sorry to bother you while treating these soldiers--\""

    hide helencry
    show helentalk1
    with dissolve

    h "\"Hulya and I were able to gather the vegetables you asked for yesterday.\""

    hide helentalk1
    show helentalk2
    with dissolve
    h "\"We left them on the kitchen--\""

    hide helentalk2
    with dissolve

    "I start to walk in the direction where the kitchen is located."

    "In the kitchen, different vegetables and fruits are found."

    show bananas
    with dissolve

    "Most of them are bananas,"

    hide bananas
    show soybeans
    with dissolve
    "and soybean fruits."

    hide soybeans
    show helentalk2
    with dissolve

    h "\"Most of these were picked from the forest--\""

    hide helentalk2
    show helentalk1
    with dissolve

    h "\"We also tried to ask from our neighbors’ farms.\""

    hide helentalk1
    show soybeans
    with dissolve

    "I picked some of the soybean fruits and immediately got the materials I needed in preparing the soybean milk drink for the soldiers."

    hide soybeans
    show helentalk1
    with dissolve

    h "\"Kapitana, I was also able to ask Mario to gather and prepare the bamboo container for the milk drink before I arrived here.\""

    hide helentalk1
    with dissolve

    "{i}After cleaning and removing the skin of the soybeans, Helen and I soaked the soybean in a bowl of water which will be left overnight."

    show helenblush
    with dissolve
    h "\"When we gathered the vegetables, farmers said that there are still shortages of tomatoes.\""

    hide helenblush
    show helencry
    with dissolve

    h "\"I cannot help myself not to worry about how we are able to feed the guerillas and the other Filipino soldiers.\""

    hide helencry
    show mariatalk
    with dissolve
    m "\"I don’t know how long the shortage in tomatoes will continue.\""

    hide mariatalk
    show helensmile
    with dissolve
    h "\"I’m glad you were able to invent alternatives for tomatoes.\""

    h "\"The people are grateful for the banana ketchup recipe you gave them.\""

    hide helensmile
    show mariasmile
    with dissolve
    "I finally look up to Helen to give her a reassuring look."

    "{i} I am terribly worried about the soldiers in the internment camps."

    "{i} They must be starving."

    hide mariasmile
    with dissolve

    scene bgkitchen2
    with fade

    show mariatalk
    with dissolve
    m "\"Helen, fetch me the dough. We’ll be making Darak.\""

    hide mariatalk
    show dough
    with dissolve
    "She hands me the chunk of dough from the countertop on the opposite side of the kitchen."

    hide dough
    show helenblush
    with dissolve

    h "\"Will this be the cookie to help the village suffering the outbreak of Beriberi?\""

    hide helenblush
    show mariasmile
    with dissolve

    m "\"Yes it will\""

    hide mariasmile
    with dissolve

    "I took the dough from Helen’s hands and started portioning them."

    "We proceeded to cook all of them in the oven."

    "I think this amount will suffice."

    scene tirelessly
    with fade

    "Helen and I worked tirelessly the entire day."

    "I’ve decided to smuggle food into the camps."

    "I cannot let the Filipinos starve to death."

    scene bgkitchen
    with fade

    "I lost track of time until I heard the roosters."

    show darakcookies
    with dissolve

    "I am done preparing the darak cookies,"

    hide darakcookies
    show soyalac
    with dissolve

    "and the soyalac. I will now put them in the bamboo containers."

    "The door creaks open and I see Helen."

    hide soyalac
    show helenangry
    with dissolve

    h "\"Kapitana, are you sure about sneaking the Soyalac into the camps?\""

    hide helenangry
    show mariaangry
    with dissolve

    m "\"I am.\""

    hide mariaangry
    show marianotalk
    with dissolve

    m "\"Please tell Mario I am grateful for his assistance.\""

    hide marianotalk
    show mariasmile
    with dissolve

    m "\"Thank you, Helen. I best be on my way now.\""

    hide mariasmile
    show helenangry
    with dissolve

    h "\"Are you sure that you want to go alone?\""

    hide helenangry
    show helentalk1
    with dissolve

    h "\"There are many of us who could accompany you.\""

    hide helentalk1
    show helenblush
    with dissolve

    h "\"It’s for your safety."

    hide helenblush
    show mariathink
    with dissolve

label alone_unalone:
        play music "audio/decision.mp3"
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'gameover'
        show screen countdown
        menu:

            "What should I do?"
            "I suppose one or two wouldn’t spark suspicion.":
                hide screen countdown
                jump unalone

            "It’s best if I go alone.":
                hide screen countdown
                jump alone

        return

label unalone:
    play music "audio/camping.mp3"
    scene bgkalesa
    with fade

    "I accepted the help that the others offered me."

    "We were able to ride a kalesa into the camps."

    scene bgcamp
    with fade

    "As it turns out, there was one gate left unguarded."

    hide mariathink
    show cloaks
    with dissolve

    "We disguised ourselves under cloaks,"

    hide cloaks
    show handout
    with dissolve

    "and gave people servings of the Soyalac and some Darak in the shadows."

    hide handout
    with dissolve

    "Fortunately, we were not seen."

    scene black
    with dissolve

    "We made it back home safely."

    scene bgcamp
    show cloaks
    with dissolve

    "This would go on for more and more days."

    hide cloaks
    show handout
    with dissolve

    "Successfully sneaking food for the Filipinos inside the camps."

    "It’s not much, but it’s everything that I can do to help keep them alive."

    jump chapter_5

label alone:

    play music "audio/camping.mp3"
    scene bgway
    with fade

    "After saying farewell to Helen and the others, I set off to internment camp."

    show men
    with dissolve

    "Carrying the heavy bamboo containers on my back, I see two figures walking towards me."

    hide men
    show cloak_alone
    with dissolve

    "I turn to face them."

    "Looking down will only incite suspicion."

    "I thought they would ignore me."

    "I was wrong."

    scene black
    with fade

    "They searched my body and discovered the Soyalac inside the bamboo containers."

    show brokensoyalac
    with dissolve
    play sound "audio/glass.mp3"

    "One of the men threw it onto the ground, spilling my hard work as waste."

    hide brokensoyalac
    scene bgprison
    with fade

    "I was sent behind bars for suspicion."

    "No longer able to help any of my countrymen."

    jump gameover

    label chapter_5:
    play music "audio/rememberme.mp3"
    $ lastsave = "chapter_5"

    scene chapcard5
    with fade
    pause

    scene bg1phamwar
    with fade
    "Years have passed, yet the war still hasn’t ended."

    scene bg1revwar
    with fade
    "Many of the Filipinos have succumbed to their deaths, while others spend their lives in turmoil."

    scene bgwar
    with fade
    "I have dedicated my life, all 52 of my years, to serving the Filipino people."

    scene bglivingroom
    with fade
    "I am sitting on the sofa of my living room with my brother, Sixto."

    "He has come to persuade me once again to flee from the chaos in Manila."

    show sixtotalkcalm
    with dissolve

    s "\"Sister, everyone in the family is worried about your welfare.\""

    hide sixtotalkcalm
    show sixtotalk
    with dissolve

    s "\"Please consider coming with us.\""

    hide sixtotalk
    show sixtoangry
    with dissolve

    s "\"The war will not leave you unscathed.\""

    hide sixtoangry
    show 5mariathink
    with dissolve

label war_home:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'gameover'
    show screen countdown
    menu:
        "What should I do?"
        "Stay in Manila.":
            hide screen countdown
            jump war

        "Come home to the family.":
            hide screen countdown
            jump home

    return
    label home:
        hide 5mariathink
        with dissolve

        "I packed my bags and got ready to go back to my hometown."

        scene black
        with fade

        "My brother and I made it safely back home."

        "Although I am happy to be with my family once more, I am haunted by the guilt of abandoning my duties as a soldier, as a chemist, and as a Filipino."

    jump gameover

    label war:
        scene bglivingroom
        show 5mariasmile
        with dissolve
        "I face my worried little brother with a smile on my face."

        hide 5mariasmile
        show mariatearsofjoy
        with dissolve

        "{i}He’s genuinely concerned."

        hide mariatearsofjoy
        show 5mariasmile
        with dissolve

        m "\"I appreciate your concern.\""

        hide 5mariasmile
        show mariatearsofjoy
        with dissolve

        m "\"I knew that I am going to meet death anytime the moment I decided to be a soldier.\""

        hide mariatearsofjoy
        show 5mariarelief
        with dissolve

        m "\"The Filipinos need me, my brother.\""

        m "\" I cannot let them down.\""

        hide 5mariarelief
        show sixtotalk
        with dissolve

        s "\"What about family?\""

        hide sixtotalk
        show sixtocry
        with dissolve

        s "\"We cannot afford to lose any more of us.\""

        hide sixtocry
        show 5mariarelief
        with dissolve

        m "\"I also cannot afford to live with being a coward when I depart from Manila.\""

        hide 5mariarelief
        show 5mariasmile
        with dissolve

        m "\"This is my duty.\""

        m "\"You know very well where I am coming from, Sixto.\""

        m "\"You yourself are a physician sworn to heal the sick.\""

        hide 5mariasmile
        show sixtoangry
        with dissolve

        s "\"But Maria--\""

        hide sixtoangry
        show 5mariarelief
        with dissolve

        m "\"Sixto, I will be fine.\""

        hide 5mariarelief
        show mariatearsofjoy
        with dissolve

        m "\"If it is time for me to go, I will go.\""

        m "\"If God decides to spare me, so be it.\""

        hide mariatearsofjoy
        show 5mariasmile
        with dissolve

        m "\"Tell our siblings that my decision is final.\""

        hide 5mariasmile
        show sixtotalkcalm
        with dissolve

        s "\"So, I came here for you to no avail?\""

        hide sixtotalkcalm
        show 5mariarelief
        with dissolve

        m "\"No, I am thankful that you care for me enough to travel all the way here.\""

        hide 5mariarelief
        show mariatearsofjoy
        with dissolve

        m "\"I love all of you so much.\""

        m "\"Please be safe.\""

        m "\"Don't worry about me.\""

        hide mariatearsofjoy
        show sixtocutscene
        with dissolve
        pause

        "I saw tears stream down my brother’s face."

        hide sixtocutscene
        show sixtocutscene2
        with dissolve
        pause

        "However, I know that I am making the right decision."

        "After seeing him off on his way home, I prayed that God will keep my family safe."

        hide sixtocutscene2

        play music "audio/death2.mp3"

        scene bgoffice
        with fade

        "As the war and bombings rage, I continue my operations at my office."

        "The skies are as dark as the times we are facing today."

        "I wonder how many more people are dying outside of these walls."

        "I must go on for their sake."

        play sound "audio/knock.mp3"
        scene bgclosedoor
        with fade
        pause

        "Suddenly, I am startled by the violent knocks on the door."

        scene bgopendoor
        with fade

        "I immediately rush to open it and I see a young man drenched in sweat, such horror in his eyes."

        show 5paramedic
        with dissolve
        pause

        c "\"Madam! Please evacuate the building!\""

        play sound "audio/bomb.mp3"

        c "\"The Americans have started a bombing raid!\""

        hide 5paramedic
        show 5mariafight
        with dissolve
        pause

        m "\"Do tell the others.\""

        m "\"I’ll be right behind you.\""

        scene black
        with fade

        "As I turn to prepare for departure, a loud pang on the walls shoots through my ears."

        hide 5mariafight
        show 5mariaground
        with dissolve

        "The next thing I know, I am on the ground, unable to move."

        "Though my vision is blurry and my head is aching, it appears that the bombs have reached my office and have brought me to my demise."

        hide 5mariaground
        scene black
        with fade

        p "\"Over here, please....gently\""

        show 5maria1
        with dissolve
        play music "audio/sad.mp3"

        "Minutes later, I am lying on a hospital bed."

        "{i}Even though I am here, why do I feel so...unsafe?"

        "{i}I guess it is safe to say that my time has come."

        hide 5maria1
        show 5maria3
        with dissolve

        "I have no regrets in this life."

        "I may not have been able to see my family on my deathbed, I am content knowing that I have lived a life of purpose."

        "I have been useful."

        "All the studies I have left unfinished, the plans that remain as words on my journals, all of these shall be taken up by someone else, one way or another."

        hide 5maria1
        show 5maria2
        with dissolve

        "Hearing more of the bomb’s impact, I shed a tear."

        "I should have come to terms with it by now, but death sure is frightening."

        "I hope that this war will end soon, and that the Filipinos will finally live in peace."

        "In a split second, I saw it all."

        "The bombings have reached my quarter, and something has pierced through my chest."

        hide 5maria2
        scene black
        with fade

        "Slowly, I feel my heart stop beating."

        "I close my eyes..."

        scene black
        with fade
        stop sound

        "Maria Orosa died on the 13th day of February in 1945."

        "The hospital she was taken to was hit by bombs, causing shrapnel to pierce her heart which killed her in an instant."

        "Maria has been recognized by the government and many organizations for her efforts."

        "She was given a humanitarian award by The American Red Cross for helping those inside the internment camps survive by smuggling food for them."

        "Helen Orosa del Rosario, Maria’s niece, published Maria Orosa: Her Life and Work in 1970."

        "The book features all 700 of Maria’s recipes which she created in her lifetime."

        "To this day, she is honored by the Filipinos, especially the people of Batangas, for her bravery, dedication, and loyalty to the country."

        "She had used all of her skills, talents, and resources to help the Filipinos."

        "In her vision, she wanted the Philippines to be independent, to be self-sustained."

        "This has been the life of the national hero, Maria Ylagan Orosa."

label credits:

scene slide1:
    zoom 1.5
with fade
pause

scene slide2:
    zoom 1.5
with fade
pause

scene slide3:
    zoom 1.5
with fade
pause

return

return

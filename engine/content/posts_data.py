# -*- coding: utf-8 -*-
"""90-day content dataset for Dr. Khizer's Facebook page (caregiver audience)."""

TAGS = "#DiabetesCare #Diabetes #Obesity #WeightLoss #HealthyIndia #DiabetesAwareness #FamilyHealth #Caregivers #SugarControl #DrKhizer #HealthyLiving #DiabetesDiet"
HARD = ("📅 If any of this feels familiar, please don’t wait and watch. "
        "Book a consultation with Dr. Khizer — appointment link is in the first comment. 👇  {{EKACARE_LINK}}")

def P(pillar, layout, kicker, accent, caption, fc, cta, time, **img):
    d = dict(pillar=pillar, layout=layout, kicker=kicker, accent=accent,
             caption=caption, fc=fc, cta=cta, tags=TAGS, time=time)
    d.update(img)
    return d

POSTS = []

# ============================ MONTH 1 (Days 1-30) ============================
POSTS += [
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“Diabetes is caused by eating too much sugar.” — This is the #1 thing families get wrong.\n\n"
  "Type 2 diabetes is mainly about how the body handles insulin over years — driven by genetics, weight, activity, sleep and stress. Sugar is a piece of the puzzle, not the whole story. A slim person who never touches sweets can still develop it; a person who loves mithai may never.\n\n"
  "Why this matters for you as a family member: blaming ‘too much sugar’ leads to shame and secret eating. Understanding the real drivers leads to teamwork.\n\n"
  "↗️ Share this with a family member who still believes the sugar myth.",
  "If you’re unsure whether a loved one is at risk, a 15-minute check gives you clarity. Book here 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Diabetes is caused by eating too much sugar.”",
  fact="Type 2 diabetes is mainly about how the body handles insulin over years — genetics, weight, activity and sleep. Sugar is one piece, not the whole story."),

P("Plate & Portion","list","On Your Plate","green",
  "You don’t have to cook two separate meals for someone with diabetes. You just have to rebalance the plate everyone already eats.\n\n"
  "The simple rule for the family thali:\n"
  "• ½ plate — vegetables and salad (start the meal here)\n"
  "• ¼ plate — protein: dal, egg, paneer, chicken, fish\n"
  "• ¼ plate — carbs: rice or 1–2 rotis\n"
  "• A katori of curd on the side\n\n"
  "Eating veg and protein first, carbs last, blunts the sugar spike after the meal — for everyone at the table.\n\n"
  "🔖 Save this and put it on the fridge.",
  "Want a diabetes-friendly meal plan built around your kitchen and budget? We can do that in a consult 👉 {{EKACARE_LINK}}",
  "Soft (Save)","12:30 PM",
  headline="Rebalance the family thali",
  lines=["½ plate — vegetables & salad (eat first)","¼ plate — protein: dal, egg, paneer, fish",
         "¼ plate — carbs: rice or 1–2 rotis","A katori of curd on the side","Carbs last = a smaller sugar spike"]),

P("Warning Signs","list","Warning Signs","red",
  "Many people with diabetes feel completely normal while their sugars quietly do damage. As the person who sees them daily, you’re often the first to notice. Watch for:\n\n"
  "1. Getting up 2–3 times at night to pass urine\n"
  "2. Unusual thirst or a dry mouth\n"
  "3. Tiredness or sleepiness after meals\n"
  "4. Slow-healing cuts, or tingling in the feet\n"
  "5. Blurred vision that comes and goes\n\n"
  "‘Feeling fine’ is not the same as ‘being in control’. The only way to know is the numbers.\n\n"
  "If you’re nodding at 2 or more of these for someone you love, it’s time for a proper review.",
  HARD,"HARD (Book)","7:30 PM",
  headline="5 signs diabetes is NOT under control",
  lines=["Waking 2–3 times at night to pass urine","Unusual thirst or a dry mouth",
         "Tiredness or sleepiness after meals","Slow-healing cuts, or tingling feet",
         "Blurred vision that comes and goes"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "One of the most common questions I get from families. Here’s a simple reference (your doctor may set different targets for elderly or high-risk patients):\n\n"
  "• Fasting sugar: about 80–130 mg/dL\n"
  "• 2 hours after a meal: under 180 mg/dL\n"
  "• HbA1c (3-month average): under 7%\n\n"
  "Numbers a little high once in a while isn’t a crisis. A pattern of high readings is the signal to act.\n\n"
  "💬 What number confuses you the most about a loved one’s reports? Ask below — I answer through the week.",
  "Bring their last report to a consult and we’ll read it together, line by line 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="What should their sugar actually be?",
  lines=["Fasting: about 80–130 mg/dL","2 hours after a meal: under 180 mg/dL",
         "HbA1c (3-month avg): under 7%","One high reading ≠ crisis","A pattern of highs = act now"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "This one is for YOU — the daughter, the son, the spouse quietly managing someone else’s health.\n\n"
  "You track the medicines. You cook the separate-ish meals. You worry at 2 AM. And nobody asks how YOU are doing.\n\n"
  "Caregiver burnout is real, and an exhausted caregiver can’t give good care. Three permissions for this week:\n"
  "• It’s okay to take one evening off without guilt.\n"
  "• It’s okay to ask a sibling to share one task.\n"
  "• It’s okay to not have all the answers — that’s what your loved one’s doctor is for.\n\n"
  "💬 If you’re a caregiver, drop a 🙌 below.",
  "If the medical side feels overwhelming, let’s simplify their plan together so you carry less 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="You can’t pour from an empty cup. An exhausted caregiver can’t give good care."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A patient once told me she couldn’t get her mother to exercise — until she stopped calling it ‘exercise’.\n\n"
  "Every evening after dinner she said, “Amma, chalo, let’s just walk and talk.” Ten minutes. No targets. Just company.\n\n"
  "Six months later that walk had grown to 30 minutes — and her mother’s sugars had come down enough that her doctor reduced one medicine. The daughter’s blood pressure improved too.\n\n"
  "The best health routine is the one you do TOGETHER. Support beats supervision.\n\n"
  "🔖 Save this as your reminder to start small tonight.",
  "Want a walking target that’s safe for your loved one’s age and health? Ask in a consult 👉 {{EKACARE_LINK}}",
  "Soft (Save)","7:00 PM",
  quote="The best health routine is the one you do together. Support beats supervision."),

P("Support Sunday","list","Support Sunday","green",
  "Sunday reset. If you’ve ever tried to ‘motivate’ a loved one about their weight and it turned into a fight — you’re not alone.\n\n"
  "What backfires: “You’ve really let yourself go.” Shame doesn’t create change; it creates secrecy.\n\n"
  "What actually helps:\n"
  "• Lead with worry, not criticism: “I want you around for a long time.”\n"
  "• Offer to do it together: “Shall we both cut evening snacks?”\n"
  "• Focus on energy and life, not the scale.\n"
  "• Make the home the easy choice.\n\n"
  "↗️ Share this with someone who needs the words this week.",
  "Sometimes a neutral third voice — the doctor’s — lands better than family. We’re happy to be that voice 👉 {{EKACARE_LINK}}",
  "Soft (Share)","11:00 AM",
  headline="Talk about weight without pushing them away",
  lines=["Lead with worry, not criticism","“I want you around for a long time”",
         "Offer to do it together","Focus on energy & life, not the scale","Make the home the easy choice"]),

# ---- Week 2 ----
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“But he’s so thin, how can he have diabetes?” I hear this every week.\n\n"
  "The truth: you can be slim on the outside and still carry fat around the organs. In South Asians especially, diabetes often shows up at a lower body weight than in Western populations.\n\n"
  "A normal-looking waistline is NOT a guarantee. Family history, a rounder tummy and low activity matter more than the bathroom scale.\n\n"
  "Why it matters: thin family members skip testing because they ‘look fine’ — and get diagnosed late.\n\n"
  "↗️ Share this with the slim relative who refuses to get tested.",
  "Not sure if someone should be screened? A quick consult settles it 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Thin people don’t get diabetes.”",
  fact="You can be slim outside and still carry fat around the organs. In South Asians, diabetes often appears at a lower body weight — a normal waistline is no guarantee."),

P("Plate & Portion","list","On Your Plate","green",
  "You don’t need expensive ‘diabetic’ products. You need small swaps in food you already buy:\n\n"
  "• White rice → add dal + veg, or try brown/hand-pounded rice a few days a week\n"
  "• Maida roti → whole-wheat or millet (bajra, jowar)\n"
  "• Fruit juice → the whole fruit (the fibre is the point)\n"
  "• Fried namkeen → roasted chana, makhana, nuts\n"
  "• Second helping of rice → second helping of sabzi\n\n"
  "Swaps beat bans. Nobody sticks to a diet that feels like punishment.\n\n"
  "🔖 Save this for your next grocery run.",
  "Want these swaps tailored to what your family actually eats? Let’s build it together 👉 {{EKACARE_LINK}}",
  "Soft (Save)","12:30 PM",
  headline="5 smart swaps in your kitchen",
  lines=["White rice → add dal + veg / brown rice","Maida roti → whole-wheat or millet",
         "Fruit juice → the whole fruit","Fried namkeen → roasted chana / makhana","Extra rice → extra sabzi"]),

P("Warning Signs","list","Warning Signs","red",
  "If someone in your home has diabetes, please read this once and remember it.\n\n"
  "A tiny cut, blister or crack on a diabetic’s foot is not a small thing. High sugar reduces sensation and slows healing — so a minor wound can quietly become a serious infection.\n\n"
  "Your weekly 2-minute caregiver check:\n"
  "• Look at the soles and between the toes (use a torch)\n"
  "• Any cut, redness, swelling, or a wound not healing in a few days\n"
  "• Never let them walk barefoot, even at home\n\n"
  "A wound that’s changing colour, smelling or spreading is an emergency.\n\n"
  "If you’ve spotted something that isn’t healing, please get it looked at now.",
  HARD,"HARD (Book)","7:30 PM",
  headline="The foot wound you must never ignore",
  lines=["Check soles & between toes weekly (use a torch)","Look for cuts, redness, swelling",
         "A wound not healing in days = act","Never walk barefoot, even at home","Spreading/smelling wound = emergency"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "A question I get almost daily. Short answer: most fruit is GOOD, in the right portion.\n\n"
  "Whole fruit comes with fibre, which slows sugar absorption. The problems start with (a) fruit JUICE and (b) very large portions.\n\n"
  "Practical rule for the family:\n"
  "• A fistful portion of whole fruit is fine for most\n"
  "• Pair it with nuts or curd to flatten the spike\n"
  "• Prefer whole fruit over juice, always\n\n"
  "💬 Which fruit are you unsure about — mango? banana? Ask below.",
  "For a personalised list of ‘yes’ and ‘go-easy’ foods for their reports, book a consult 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="Is fruit bad for diabetics?",
  lines=["Most whole fruit is GOOD, in portion","A fistful portion is fine for most",
         "Pair with nuts or curd to flatten the spike","Whole fruit beats juice, always","Go easy on very sweet, large portions"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "There’s a job with no title that millions of family members do: remembering someone else’s medicines, refills, appointments and reports.\n\n"
  "It’s mentally exhausting. A few things that lighten the load:\n"
  "• A weekly pill organiser (7-day box) — fill it every Sunday\n"
  "• One phone alarm per dose, named clearly\n"
  "• A single photo album for all their reports\n"
  "• Book the next appointment before you leave the current one\n\n"
  "You’re doing more than anyone sees. 🔖 Save these four fixes.",
  "We can simplify their prescription to fewer, easier doses where possible — ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","9:00 PM",
  quote="Being someone’s human medicine reminder is an invisible job. Systems make it lighter — you don’t have to hold it all in your head."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A gentleman came to me convinced he’d have to ‘starve’ to lose weight. He was so scared of it, he never started.\n\n"
  "We didn’t start with a diet. We started with three things: a 20-minute after-dinner walk, swapping his second helping of rice for sabzi, and cutting two sugary teas down to one.\n\n"
  "No drama. No hunger. Four months later — 6 kg lighter, better sleep, and his pre-diabetes numbers back in the safe zone.\n\n"
  "Small, boring, repeatable changes win.\n\n"
  "↗️ Share this with someone who thinks they must suffer to get healthier.",
  "Want a realistic, no-starvation plan for your loved one? That’s exactly what we do 👉 {{EKACARE_LINK}}",
  "Soft (Share)","7:00 PM",
  quote="6 kg down — no crash diet, no gym. Small, boring, repeatable changes beat dramatic ones every time."),

P("Support Sunday","list","Support Sunday","green",
  "Sunday idea: do ONE grocery trip together with new eyes. What comes into the house decides what everyone eats all week.\n\n"
  "The together-reset:\n"
  "• Front of the fridge: cut fruit, curd, salad — the easy grab\n"
  "• Pantry: roasted chana / makhana / nuts instead of fried snacks\n"
  "• Atta shelf: add one millet (bajra or jowar)\n"
  "• Checkout rule: for every sweet/fried item, add one veg or fruit\n\n"
  "Do it as a team, not a diet imposed on one person.\n\n"
  "🔖 Save this as your shopping checklist.",
  "Want a ‘green list / go-easy list’ tailored to your loved one’s condition? We’ll make it in a consult 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="A family grocery reset",
  lines=["Fridge front: cut fruit, curd, salad","Pantry: roasted chana / makhana over fried",
         "Atta shelf: add one millet","Checkout: 1 sweet/fried → add 1 veg/fruit","Shop as a team, not a punishment"]),

# ---- Week 3 ----
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "So many families resist insulin because they think it’s a punishment or a sign of ‘giving up’. This belief delays good care — and that delay does real harm.\n\n"
  "The truth: for many people, the pancreas simply makes less insulin over time. Taking insulin isn’t failure — it’s giving the body the exact thing it’s short of. It often protects the kidneys, eyes and nerves far better than struggling on tablets alone.\n\n"
  "Insulin today is easy — tiny needles, simple pens. The fear is almost always bigger than the reality.\n\n"
  "↗️ Share this with a family that’s scared of the word ‘insulin’.",
  "If insulin has been suggested for your loved one and you have doubts, let’s talk it through calmly 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Starting insulin means you’ve failed.”",
  fact="For many, the pancreas simply makes less insulin over time. Insulin isn’t failure — it’s giving the body what it’s short of, and it protects the eyes, kidneys and nerves."),

P("Plate & Portion","list","On Your Plate","green",
  "That ‘sugar-free’ biscuit or ‘diet’ namkeen isn’t the free pass families think it is.\n\n"
  "‘Sugar-free’ often just means no added table sugar — but it’s still refined flour and fat, which also raise sugar and weight. ‘Diet’ and ‘baked’ are marketing words, not medical ones.\n\n"
  "What to actually check on the packet:\n"
  "• Total carbohydrate (not just ‘sugar’)\n"
  "• The first 2–3 ingredients (maida/palm oil near the top = go easy)\n"
  "• Serving size — the ‘low’ number is often for 2 biscuits\n\n"
  "Real food with no label usually beats anything marketed as ‘diabetic-friendly’.\n\n"
  "🔖 Save this for your next supermarket trip.",
  "Confused by a specific product? Bring it to a consult and we’ll decode the label together 👉 {{EKACARE_LINK}}",
  "Soft (Save)","12:30 PM",
  headline="What ‘sugar-free’ really means",
  lines=["‘Sugar-free’ ≠ carb-free (still maida & fat)","Check TOTAL carbohydrate, not just sugar",
         "Read the first 2–3 ingredients","Check the real serving size","Unlabelled real food usually wins"]),

P("Warning Signs","list","Warning Signs","red",
  "If a loved one carries extra weight AND snores heavily, gasps, or stops breathing for moments in sleep — please take it seriously.\n\n"
  "This can be obstructive sleep apnea. It strains the heart, spikes blood pressure, worsens diabetes and leaves them exhausted all day.\n\n"
  "Signs the family notices first:\n"
  "• Loud snoring with pauses, then a gasp\n"
  "• Morning headaches, dry mouth\n"
  "• Falling asleep during the day, mid-conversation\n"
  "• Breathlessness on mild exertion\n\n"
  "This is treatable — but it needs proper assessment.\n\n"
  "If this sounds like someone at home, please get them evaluated.",
  HARD,"HARD (Book)","7:30 PM",
  headline="When weight becomes a night-time emergency",
  lines=["Loud snoring with pauses, then a gasp","Morning headaches, dry mouth",
         "Falling asleep during the day","Breathlessness on mild exertion","Sleep apnea is treatable — assess it"]),

P("Ask the Doctor","list","Ask the Doctor","red",
  "This is one every diabetic family must know: it may be a LOW sugar (hypoglycemia), and it can be dangerous if ignored.\n\n"
  "Warning signs of a low: sudden sweating, shakiness, hunger, confusion, irritability, dizziness — often before a meal or after extra activity.\n\n"
  "The 15-15 rule:\n"
  "• Give 15g fast sugar — 3 glucose tabs, ½ cup juice, or 1 tbsp sugar/honey\n"
  "• Wait 15 minutes, re-check\n"
  "• Still low or drowsy → emergency, get help now\n\n"
  "Keep sugar sachets in the bag, car and by the bed.\n\n"
  "💬 Have you ever managed a low at home? Tell us below.",
  "Frequent lows can mean the medicine dose needs adjusting — please don’t ignore it. Book a review 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="Shaky & sweaty? The 15-15 rule",
  lines=["Signs of a low: sweating, shaking, confusion","Give 15g fast sugar (juice / glucose tabs)",
         "Wait 15 minutes, then re-check","Still low or drowsy → emergency","Keep sugar in bag, car & by the bed"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "If you care for someone with a long-term condition, you’ve probably lain awake asking: am I doing enough? Did I miss something? Is this my fault?\n\n"
  "Here’s the truth from the other side of the clinic desk: the very fact that you’re worrying means you’re already doing more than enough. Guilt is not a measure of your failure — it’s a measure of your love.\n\n"
  "You are not responsible for controlling every number. Share the medical weight with us — that’s our job.\n\n"
  "💬 To every caregiver reading this: drop a ❤️.",
  "Feeling lost about the ‘right’ next step for your loved one? Let’s map it out together 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="Guilt is not a measure of your failure — it’s a measure of your love. If you’re worrying, you’re already doing enough."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A father was diagnosed with pre-diabetes. Instead of letting him face it alone, his son said, “Let’s both do this.” The son wasn’t even diabetic — he just refused to let his dad feel singled out.\n\n"
  "They walked at 6:30 every morning. They cut shared evening sweets to weekends. They cooked one rebalanced dinner for the whole house.\n\n"
  "At the next review, the father’s numbers were back in normal range — and the son had lost his own belly weight.\n\n"
  "Pre-diabetes is often reversible, and easier when nobody does it alone.\n\n"
  "↗️ Share this with the family member you’d do it with.",
  "If a loved one has been told ‘borderline’ or ‘pre-diabetic’, now is the window to act 👉 {{EKACARE_LINK}}",
  "Soft (Share)","7:00 PM",
  quote="A father reversed his pre-diabetes — because his son said “let’s both do this.” Nobody should do it alone."),

P("Support Sunday","list","Support Sunday","green",
  "You can’t follow your loved one around all day — but you CAN design the home so the healthy choice is the easy one. This Sunday:\n\n"
  "• Kitchen: cut fruit & salad at eye level; fried snacks out of sight\n"
  "• Routine: fix meal times; one family walk slot\n"
  "• Medicine corner: pill box, glucometer, sugar sachet — all in one place\n"
  "• Footwear: soft slippers by the bed (no barefoot walking)\n"
  "• Reports: one folder, newest on top\n\n"
  "Environment beats willpower. Fix the home once.\n\n"
  "🔖 Save this Sunday setup checklist.",
  "Want us to review their current routine and fine-tune it? Bring it to a consult 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="Make your home diabetes-friendly",
  lines=["Kitchen: fruit & salad at eye level","Fix meal times + one family walk slot",
         "One medicine corner: pills, glucometer, sugar","Soft slippers by the bed (no barefoot)","One reports folder, newest on top"]),

# ---- Week 4 ----
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "When a loved one struggles to lose weight, it’s easy to think they’re just not trying hard enough. That belief is unfair — and wrong.\n\n"
  "Weight is driven by hormones, genetics, sleep, stress, medicines, gut health and years of habit — not willpower alone. The body actively fights to hold on to weight. That’s biology, not weakness.\n\n"
  "‘Just try harder’ makes people give up in shame. Understanding it’s medical opens the door to real help.\n\n"
  "↗️ Share this with someone made to feel it’s all their fault.",
  "Struggling weight often has a treatable cause. Let’s find it together 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Losing weight is just willpower.”",
  fact="Weight is driven by hormones, genetics, sleep, stress and medicines — not willpower alone. The body actively fights to hold on to weight. That’s biology, not weakness."),

P("Plate & Portion","list","On Your Plate","green",
  "Festivals and sweets go together — and telling a diabetic loved one ‘no’ just makes everyone miserable. Here’s the kinder, smarter way:\n\n"
  "• Pick ONE favourite sweet, a small portion, eaten slowly\n"
  "• Have it right after a meal (not empty stomach) to soften the spike\n"
  "• Add a family walk after the feast\n"
  "• Portion mithai into small pieces before serving\n"
  "• Send leftover boxes to neighbours\n\n"
  "One festive day won’t undo good habits. It’s the everyday that counts.\n\n"
  "🔖 Save this before the next celebration.",
  "Want a ‘festival game plan’ for your loved one’s condition? Ask in a consult 👉 {{EKACARE_LINK}}",
  "Soft (Save)","12:30 PM",
  headline="Enjoy festival sweets without the guilt",
  lines=["Pick ONE favourite, small portion, slowly","Eat it after a meal, not empty stomach",
         "Add a family walk after the feast","Cut mithai into small pieces first","Send leftovers to neighbours"]),

P("Warning Signs","list","Warning Signs","red",
  "High sugar doesn’t always shout. Often it whispers — and because you see your loved one daily, small changes are easy to miss:\n\n"
  "• Drinking a lot more water, dry mouth\n"
  "• Waking at night to urinate, more than before\n"
  "• Unexplained weight loss despite eating normally\n"
  "• Wounds or mouth ulcers healing slowly\n"
  "• More frequent infections (skin, urine, gums)\n"
  "• New irritability or brain fog\n\n"
  "Any of these creeping in over weeks deserves a sugar check.\n\n"
  "If two or more ring true, it’s time to get their numbers checked.",
  HARD,"HARD (Book)","7:30 PM",
  headline="The ‘silent’ high-sugar signs",
  lines=["Much more thirst, dry mouth","Waking at night to urinate more",
         "Unexplained weight loss","Slow-healing wounds / mouth ulcers","Frequent infections; new brain fog"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "HbA1c is the ‘3-month report card’ of diabetes — the average control, not just one day. Families often don’t know how often it’s needed.\n\n"
  "General guide (your doctor personalises this):\n"
  "• Well controlled & stable: about every 6 months\n"
  "• Newly diagnosed / medicines changing / not in target: every 3 months\n"
  "• No fasting needed — any time of day\n\n"
  "A single fasting sugar can look fine while the 3-month average is high. That’s why HbA1c matters.\n\n"
  "💬 When did your loved one last do an HbA1c?",
  "Not sure which tests are due? We’ll set up a simple monitoring schedule 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="How often to check HbA1c?",
  lines=["It’s the 3-month average, not one day","Stable & controlled: ~every 6 months",
         "Changing meds / not in target: every 3 months","No fasting needed, any time","Catches what daily checks miss"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "Few things are more painful than watching someone you love ignore advice that could help them.\n\n"
  "First, breathe. Their choices are not a verdict on your love or effort. You can lead a person to care; you cannot force them to accept it.\n\n"
  "What works better than nagging:\n"
  "• One change at a time, not a lecture\n"
  "• Connect health to what THEY value\n"
  "• Let the doctor deliver the hard message\n"
  "• Celebrate the small ‘yes’\n\n"
  "💬 What finally got your loved one to take one step?",
  "Sometimes they’ll hear it from a doctor when they won’t from family 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="You can lead a person to care; you cannot force them to accept it. Their choices are not a verdict on your love."),

P("Small Wins / Story","quote","A Real Story","teal",
  "🇮🇳 On Independence Day, here’s a different freedom worth fighting for: freedom from uncontrolled sugar, from constant tiredness, from the fear of complications.\n\n"
  "One of my patients calls her morning walk her ‘azaadi hour’ — the one hour that keeps her strong for her grandchildren. Her HbA1c came down not with a miracle, but with a family that made small changes routine.\n\n"
  "Real independence, later in life, is being able to move, remember and live without depending on anyone.\n\n"
  "💬 Wish someone their ‘azaadi hour’ below.",
  "Ready to help a loved one take back control? A consult is a great first step 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 AM",
  quote="Real independence, later in life, is being able to move, remember and live without depending on anyone. Good control today buys that freedom."),

P("Support Sunday","list","Support Sunday","green",
  "Most exercise plans die in week two because they rely on one person’s motivation. Family routines survive because they rely on each other. This Sunday, set up a walk the household can keep:\n\n"
  "• Anchor it to something fixed — right after dinner\n"
  "• Start absurdly small — 10 minutes\n"
  "• Pair up — nobody skips when someone’s waiting\n"
  "• Make it pleasant — chat, music, a nice route\n"
  "• Track it — a tick on a shared calendar\n\n"
  "Consistency beats intensity.\n\n"
  "🔖 Save this and pick your family’s walk time tonight.",
  "Want a safe activity target for a loved one with heart, joint or sugar issues? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="A family walk the whole house keeps",
  lines=["Anchor it right after dinner","Start absurdly small — 10 minutes",
         "Pair up so nobody skips","Make it pleasant — chat, music","Track it on a shared calendar"]),

# ---- Days 29-30 ----
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "When diabetes or obesity runs in the family, it’s tempting to feel it’s ‘destiny’ — that effort is pointless. This belief quietly stops people from even trying.\n\n"
  "The hopeful truth: family history loads the gun, but lifestyle pulls the trigger. Genes raise the risk — they don’t seal the fate. People with strong family history routinely delay or avoid diabetes for years with the right habits.\n\n"
  "So if it’s in your family, that’s a reason to start earlier — not to give up.\n\n"
  "↗️ Share this with a relative who thinks it’s ‘hopeless anyway’.",
  "Strong family history? Early screening changes everything. Book a check for a loved one 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“It runs in our family, so nothing I do matters.”",
  fact="Family history loads the gun, but lifestyle pulls the trigger. Genes raise risk — they don’t seal fate. The right habits delay or avoid diabetes for years."),

P("Plate & Portion","list","On Your Plate","green",
  "One month of small changes, in one place. If you save a single post from this page, make it this one:\n\n"
  "🍽️ The plate: ½ veg, ¼ protein, ¼ carbs — veg first\n"
  "🔁 Swaps beat bans: whole fruit over juice, roasted over fried\n"
  "🚶 The 10-minute family walk after dinner\n"
  "👣 Weekly foot check for anyone with diabetes\n"
  "📋 One folder for reports; know the next HbA1c date\n"
  "❤️ Support beats supervision\n\n"
  "You don’t need a perfect plan — just a repeatable one.\n\n"
  "🔖 Save this. ↗️ Share it with another caregiver.",
  "When you’re ready to turn these habits into a plan built for your loved one, we’re here 👉 {{EKACARE_LINK}}",
  "Soft (Save/Share)","12:30 PM",
  headline="Your 30-day cheat sheet",
  lines=["Plate: ½ veg, ¼ protein, ¼ carbs — veg first","Swaps beat bans","10-minute family walk after dinner",
         "Weekly foot check for diabetics","One reports folder + next HbA1c date","Support beats supervision"]),
]

# ============================ MONTH 2 (Days 31-60) ============================
POSTS += [
# Week 5
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“A diabetic can never eat rice.” This scares families into miserable, unsustainable meals.\n\n"
  "The truth: it’s not rice vs no-rice — it’s how much, and what’s with it. A moderate portion of rice, eaten after vegetables and protein, with dal and curd, behaves very differently from a big bowl of plain rice alone.\n\n"
  "Banning a staple usually backfires; balancing it lasts.\n\n"
  "↗️ Share this with the family who thinks rice is ‘forbidden’.",
  "Want the right rice portion for your loved one’s numbers? We’ll set it in a consult 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“A diabetic can never eat rice.”",
  fact="It’s not rice vs no-rice — it’s how much and what’s with it. A moderate portion after veg and protein, with dal and curd, behaves very differently from a big plain bowl."),

P("Plate & Portion","list","On Your Plate","green",
  "Breakfast sets the whole day’s sugar. A good one keeps a loved one full and steady till lunch. Family-friendly options:\n\n"
  "• Veg poha or upma with peanuts + a boiled egg on the side\n"
  "• Besan/moong chilla with chutney\n"
  "• Curd + fruit + a handful of nuts\n"
  "• 2 eggs any style + 1 whole-wheat toast\n\n"
  "The pattern: some protein + fibre, not just carbs alone.\n\n"
  "🔖 Save these for busy mornings.",
  "Want a week of diabetes-friendly breakfasts for your household? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","9:00 AM",
  headline="4 steady-sugar breakfasts",
  lines=["Veg poha/upma + peanuts + a boiled egg","Besan or moong chilla with chutney",
         "Curd + fruit + a handful of nuts","2 eggs + 1 whole-wheat toast","Always pair protein + fibre with carbs"]),

P("Warning Signs","list","Warning Signs","red",
  "Diabetes can quietly affect the eyes long before vision feels ‘bad’. As a family member, watch for changes a loved one may brush off:\n\n"
  "• Blurred or fluctuating vision\n"
  "• Difficulty reading or seeing at night\n"
  "• Dark spots or ‘floaters’\n"
  "• Frequent changes of spectacle power\n\n"
  "Uncontrolled sugar is a leading cause of preventable blindness — but a yearly eye check catches it early.\n\n"
  "If a loved one hasn’t had an eye check this year, please arrange one.",
  HARD,"HARD (Book)","7:30 PM",
  headline="Diabetes and the eyes",
  lines=["Blurred or fluctuating vision","Trouble reading or seeing at night",
         "Dark spots or ‘floaters’","Spectacle power changing often","A yearly eye check catches it early"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“Can diabetes actually be reversed?” — a hopeful question I love.\n\n"
  "For many with early type 2 or pre-diabetes, the answer is: it can often be pushed into remission — normal sugars without medicines — especially with meaningful weight loss and activity. The earlier you act, the better the odds.\n\n"
  "It’s not a guaranteed ‘cure’, and it needs medical guidance — but for a lot of families, real improvement is very possible.\n\n"
  "💬 Has a loved one been told ‘borderline’? That’s the best time to act — tell me below.",
  "Want to know if remission is realistic for your loved one? Let’s assess it together 👉 {{EKACARE_LINK}}",
  "HARD (Book)","8:00 PM",
  headline="Can diabetes be reversed?",
  lines=["Early type 2 / pre-diabetes can often go into remission","Normal sugars without medicines is possible",
         "Weight loss + activity drive it","The earlier you act, the better the odds","Needs medical guidance, not guesswork"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "You book their appointments. You remember their reports. When did YOU last see a doctor?\n\n"
  "Caregivers quietly postpone their own health for years — and that’s how the carer becomes the next patient. Your check-ups, your sleep, your blood pressure matter too.\n\n"
  "This week’s ask is simple: book one thing for yourself. A check-up, a walk, an early night.\n\n"
  "💬 Promise yourself one small thing — type it below to make it real.",
  "Looking after a loved one’s diabetes AND want your own numbers checked? We see caregivers too 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="Caregivers postpone their own health for years — and that’s how the carer becomes the next patient. Book one thing for yourself this week."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A grandmother told me her only goal was to lift her grandson without her knees screaming.\n\n"
  "We didn’t chase a number on the scale. We worked on gentle daily movement, more protein, and steadier sugars. Six months on, she’s down a little weight, off one painkiller — and she lifts him every evening.\n\n"
  "Health goals don’t have to be grand. They just have to matter to the person.\n\n"
  "🔖 Save this and ask your loved one: what’s YOUR grandson-moment?",
  "Want a goal-based plan built around what your loved one cares about? That’s how we work 👉 {{EKACARE_LINK}}",
  "Soft (Save)","7:00 PM",
  quote="Health goals don’t have to be grand. They just have to matter — like lifting your grandson without your knees screaming."),

P("Support Sunday","list","Support Sunday","green",
  "Cooking two separate meals burns out the cook and singles out the patient. The fix: one meal, gently upgraded, for everyone.\n\n"
  "• Build every meal around veg + protein first\n"
  "• Serve carbs in the katori, not piled on the plate\n"
  "• Cook once — no ‘special diabetic dish’ apart\n"
  "• Let everyone eat the same; only portions differ\n\n"
  "When the whole family eats well, the patient never feels punished.\n\n"
  "🔖 Save this and cook one family meal this way tonight.",
  "Want your regular recipes tweaked to be diabetes-friendly for all? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="One meal for the whole family",
  lines=["Build meals around veg + protein first","Serve carbs in a katori, not piled",
         "Cook once — no separate ‘diabetic dish’","Same food, only portions differ","Nobody feels singled out"]),

# Week 6
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“Only sweets raise blood sugar.” This lets a lot of hidden sugar slip past families.\n\n"
  "The truth: all carbohydrates become sugar in the body — rice, roti, bread, potato, biscuits, even ‘healthy’ juices. Sweets are obvious; the quiet carbs add up unnoticed.\n\n"
  "That’s why portion and balance matter more than just ‘cutting sweets’.\n\n"
  "↗️ Share this with someone who only watches the mithai.",
  "Want help spotting the hidden carbs in your family’s meals? We’ll map it in a consult 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Only sweets raise blood sugar.”",
  fact="All carbohydrates become sugar — rice, roti, bread, potato, biscuits, even juices. Sweets are obvious; the quiet carbs add up unnoticed."),

P("Plate & Portion","list","On Your Plate","green",
  "Eating out doesn’t have to wreck a loved one’s week. A little strategy keeps it enjoyable AND kind to their sugar:\n\n"
  "• Start with a soup or salad\n"
  "• Choose tandoori/grilled over fried/creamy\n"
  "• Share the rice/naan; double the sabzi/dal\n"
  "• Drink water or chaas, not sweet drinks\n"
  "• Take a short walk after\n\n"
  "One smart meal out beats a guilty one avoided.\n\n"
  "🔖 Save this for the next family dinner.",
  "Want a simple ‘restaurant rulebook’ for your loved one? Ask in a consult 👉 {{EKACARE_LINK}}",
  "Soft (Save)","12:30 PM",
  headline="Eating out, made diabetes-smart",
  lines=["Start with soup or salad","Tandoori/grilled over fried/creamy",
         "Share the rice/naan; double the dal","Water or chaas, not sweet drinks","Take a short walk after"]),

P("Warning Signs","list","Warning Signs","red",
  "The kidneys often suffer silently in diabetes — no pain until late. Families can catch early clues:\n\n"
  "• Swelling in the feet, ankles or around the eyes\n"
  "• Frothy or foamy urine\n"
  "• Needing to urinate much more at night\n"
  "• Rising blood pressure, tiredness, poor appetite\n\n"
  "A simple urine + blood test spots kidney strain early, when it’s most manageable.\n\n"
  "If you’ve noticed swelling or foamy urine in a loved one, please get it checked.",
  HARD,"HARD (Book)","7:30 PM",
  headline="The kidneys suffer silently",
  lines=["Swelling in feet, ankles or around eyes","Frothy or foamy urine",
         "Urinating much more at night","Rising BP, tiredness, poor appetite","A simple test catches it early"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“Is a walk after meals really that useful?” Yes — it’s one of the most underrated tools.\n\n"
  "A 10–15 minute walk after a meal helps the muscles soak up sugar, blunting the post-meal spike. It’s simple, free, and works for almost everyone.\n\n"
  "• Even a slow stroll counts\n"
  "• After the biggest meal matters most\n"
  "• Do it together and it actually sticks\n\n"
  "💬 What time is your family’s post-dinner walk? Commit to one below.",
  "Want a safe, personalised activity plan for a loved one? Let’s build it 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="Does a walk after meals help?",
  lines=["Yes — muscles soak up sugar as you walk","10–15 minutes blunts the post-meal spike",
         "Even a slow stroll counts","After the biggest meal matters most","Do it together and it sticks"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "Denial isn’t stubbornness — it’s often fear wearing a brave face. When a loved one says “I’m fine, don’t fuss,” they may be scared of what’s true.\n\n"
  "Pushing harder usually raises the wall. What lowers it: patience, small honest conversations, and letting them keep their dignity.\n\n"
  "You don’t have to win the argument today. You just have to keep the door open.\n\n"
  "💬 Have you faced denial in someone you love? You’re not alone — share below.",
  "Sometimes a calm doctor’s conversation breaks the denial gently. We can help 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="Denial isn’t stubbornness — it’s often fear wearing a brave face. You don’t have to win today; just keep the door open."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A man in his 40s was stunned to hear he had a ‘fatty liver’ — he barely drank. What he didn’t know: sugar and refined carbs can quietly fatten the liver too.\n\n"
  "No dramatic diet. He cut sugary drinks, walked daily, and lost 7% of his weight over months. His next scan and reports improved markedly.\n\n"
  "Fatty liver, caught early, is one of the most reversible conditions there is.\n\n"
  "↗️ Share this with someone who thinks ‘fatty liver’ only comes from alcohol.",
  "Told a loved one has fatty liver? Early action reverses a lot 👉 {{EKACARE_LINK}}",
  "HARD (Book)","7:00 PM",
  quote="Fatty liver, caught early, is one of the most reversible conditions there is — and sugar, not just alcohol, can cause it."),

P("Support Sunday","list","Support Sunday","green",
  "Nagging about medicines rarely works — it makes everyone tense. Gentle systems work far better. This Sunday, set up medicine support that doesn’t feel like policing:\n\n"
  "• Fill a 7-day pill box together every Sunday\n"
  "• Link doses to daily anchors (after breakfast, with dinner)\n"
  "• One shared alarm, not repeated reminders\n"
  "• Keep a small refill buffer so you never run out\n\n"
  "Support the routine, not just the person — it protects the relationship too.\n\n"
  "🔖 Save this and set it up today.",
  "Want their prescription simplified to fewer daily doses? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="Medicine support without nagging",
  lines=["Fill a 7-day pill box together on Sundays","Link doses to meals (anchors)",
         "One shared alarm, not repeated reminders","Keep a refill buffer","Support the routine, not police the person"]),

# Week 7
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“If my sugar is normal now, I can stop the medicines.” This is how many people relapse.\n\n"
  "The truth: normal sugar often means the medicines are WORKING — not that the diabetes is gone. Stopping suddenly, without your doctor, can send sugars climbing back, sometimes worse than before.\n\n"
  "Any change in dose should be a medical decision, not a self-experiment.\n\n"
  "↗️ Share this with a relative tempted to quit their tablets.",
  "Wondering if a loved one’s dose can safely be reduced? That’s a conversation to have with us 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Sugar is normal now, so I can stop my medicines.”",
  fact="Normal sugar usually means the medicines are working — not that diabetes is gone. Stopping on your own can send sugars climbing back, sometimes worse."),

P("Plate & Portion","list","On Your Plate","green",
  "Late-night snacking quietly sabotages a loved one’s sugar and sleep. If hunger hits at night, aim for smart, not sweet:\n\n"
  "• A small bowl of curd or a glass of chaas\n"
  "• A handful of nuts or roasted chana\n"
  "• Cucumber/carrot sticks\n"
  "• Warm water or unsweetened milk\n\n"
  "And check: is it real hunger, or habit, boredom, or thirst?\n\n"
  "🔖 Save this and keep these on hand instead of biscuits.",
  "Late-night hunger can signal sugar swings — worth reviewing. Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","9:00 PM",
  headline="Smart late-night snacks",
  lines=["A small bowl of curd or a glass of chaas","A handful of nuts or roasted chana",
         "Cucumber / carrot sticks","Warm water or unsweetened milk","Check: real hunger, or habit/thirst?"]),

P("Warning Signs","list","Warning Signs","red",
  "Numbness and tingling in the feet or hands is not ‘just age’ — in diabetes it can be nerve damage (neuropathy) from high sugar.\n\n"
  "Watch for a loved one mentioning:\n"
  "• Tingling, burning or ‘pins and needles’\n"
  "• Numbness — not feeling a stone in the slipper\n"
  "• Pain that’s worse at night\n"
  "• Weakness or unsteadiness\n\n"
  "Caught early, progression can be slowed. Ignored, it raises the risk of unnoticed foot injuries.\n\n"
  "If a loved one has these, please don’t dismiss it as ageing.",
  HARD,"HARD (Book)","7:30 PM",
  headline="Tingling feet isn’t ‘just age’",
  lines=["Tingling, burning or pins-and-needles","Numbness — not feeling a stone in the slipper",
         "Pain worse at night","Weakness or unsteadiness","Caught early, it can be slowed"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“Are millets really better than rice for diabetics?” A fair question with a balanced answer.\n\n"
  "Millets (bajra, jowar, ragi) bring more fibre and a gentler sugar rise than white rice — a good addition. But they’re not magic: portion still matters, and ‘millet’ biscuits or sugary ragi drinks aren’t health foods.\n\n"
  "• Swap SOME meals to millets, not all\n"
  "• Whole millet rotis/khichdi beat processed millet snacks\n\n"
  "💬 Which millet does your family cook most? Tell me below.",
  "Want a simple millet-and-rice balance for your loved one? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="Millets vs rice — the honest answer",
  lines=["Millets: more fibre, gentler sugar rise","A good addition — not magic",
         "Portion still matters","Swap SOME meals, not all","Whole millet beats millet biscuits"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "The bills, the tests, the medicines — chronic illness has a money weight that few talk about, and the caregiver often carries it silently.\n\n"
  "A few things that help: ask the doctor for generic or fewer medicines where safe, prioritise the tests that truly change decisions, and don’t be shy to discuss cost openly with your care team. Good care can be practical care.\n\n"
  "You’re allowed to ask ‘is there a more affordable way?’ — a good doctor welcomes it.\n\n"
  "💬 This one’s heavy. Send a 💙 if it resonates.",
  "Want a plan that’s effective AND mindful of cost? Let’s talk openly 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="You’re allowed to ask ‘is there a more affordable way?’ — a good doctor welcomes it. Good care can be practical care."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A retired teacher had given up on strength — ‘weights aren’t for people my age’. We started with resistance bands and a chair, ten minutes, three times a week.\n\n"
  "Months later she climbs stairs without holding the rail, her sugars are steadier, and she feels years younger. Muscle isn’t just strength — it helps the body handle sugar.\n\n"
  "It’s never too late to get stronger.\n\n"
  "🔖 Save this and share it with an older loved one who thinks strength training isn’t for them.",
  "Want safe strength exercises suited to a loved one’s age and health? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","7:00 PM",
  quote="Muscle isn’t just strength — it helps the body handle sugar. It’s never too late to get stronger."),

P("Support Sunday","list","Support Sunday","green",
  "Festivals are family time — not the enemy of health. With a plan, a loved one enjoys the day AND stays well:\n\n"
  "• Eat a normal meal before the feasting starts (never arrive starving)\n"
  "• Agree a ‘one sweet, savoured’ plan together\n"
  "• Keep them hydrated between rounds of food\n"
  "• Build in a group walk — make it tradition\n"
  "• Don’t police; support quietly\n\n"
  "Joy and health can share the same table.\n\n"
  "🔖 Save this before the festive season.",
  "Want a festival plan for your loved one’s condition and medicines? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="Enjoy festivals as a family",
  lines=["Eat a normal meal before feasting begins","Agree ‘one sweet, savoured’ together",
         "Keep them hydrated between food","Build in a group walk — make it tradition","Support quietly; don’t police"]),

# Week 8
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“Obesity is just about looks.” This myth stops people from getting real help.\n\n"
  "The truth: obesity is a recognised medical condition that drives diabetes, high blood pressure, heart disease, joint damage, sleep apnea and more. It’s not vanity — it’s health, mobility and years of life.\n\n"
  "Treating it deserves the same seriousness (and kindness) as any other condition.\n\n"
  "↗️ Share this to help someone see it’s about health, not appearance.",
  "Want to approach a loved one’s weight as a health issue, with real support? We’re here 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Obesity is just about looks.”",
  fact="Obesity is a medical condition that drives diabetes, high BP, heart disease, joint damage and sleep apnea. It’s about health and mobility — not appearance."),

P("Plate & Portion","list","On Your Plate","green",
  "The cooking oil and how much you use quietly shapes a family’s weight and heart health. Small kitchen habits, big difference:\n\n"
  "• Measure oil with a spoon, don’t pour freely\n"
  "• Rotate oils; avoid deep-frying as routine\n"
  "• Bake, roast, air-fry or sauté more often\n"
  "• Watch ‘invisible’ fat: farsan, chips, gravies\n\n"
  "You don’t need zero oil — just mindful oil.\n\n"
  "🔖 Save this for whoever runs your kitchen.",
  "Want your family’s cooking reviewed for heart-and-sugar health? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","12:30 PM",
  headline="Mindful oil in the kitchen",
  lines=["Measure oil with a spoon, don’t free-pour","Avoid routine deep-frying",
         "Bake, roast, air-fry or sauté more","Watch invisible fat: farsan, gravies","Not zero oil — mindful oil"]),

P("Warning Signs","list","Warning Signs","red",
  "Very high sugar can become an emergency, especially during an illness or infection. Families should know the red flags:\n\n"
  "• Excessive thirst + urinating a lot\n"
  "• Nausea, vomiting, stomach pain\n"
  "• Deep, fast breathing; fruity-smelling breath\n"
  "• Drowsiness or confusion\n\n"
  "These can signal a dangerous state (DKA) needing urgent care — do not wait it out at home.\n\n"
  "If a loved one shows these, seek medical help immediately.",
  HARD,"HARD (Book)","7:30 PM",
  headline="When high sugar is an emergency",
  lines=["Excessive thirst + heavy urination","Nausea, vomiting, stomach pain",
         "Deep fast breathing; fruity breath","Drowsiness or confusion","Don’t wait — seek urgent care"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“Does my loved one need to prick their finger every day?” Not always — it depends.\n\n"
  "• On insulin or unstable sugars: more frequent checks help\n"
  "• Stable on tablets: your doctor may advise fewer, structured checks\n"
  "• What matters is checking at useful times (fasting, 2-hrs after a meal) and noting patterns, not random pricks\n\n"
  "More data isn’t always better — the right data is.\n\n"
  "💬 How often does your loved one check? Ask if that’s right below.",
  "Want a simple, personalised monitoring schedule? We’ll set one up 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="Check sugar every day?",
  lines=["On insulin/unstable: more checks help","Stable on tablets: fewer, structured checks",
         "Check at useful times, note patterns","Random pricks add little","The right data beats more data"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "You lie awake listening for their cough, their movement, the alarm for the next dose. Caregiver sleep is one of the first things to go — and one of the most important to protect.\n\n"
  "Poor sleep frays patience, judgement and health. Share the night duty where you can, use simple systems so you’re not the only alarm, and give yourself permission to rest.\n\n"
  "You matter in this story too.\n\n"
  "💬 Caregivers — how are YOU sleeping? Be honest below.",
  "Exhausted from caregiving and want your own health looked at? We see caregivers too 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="Caregiver sleep is the first thing to go and the most important to protect. You matter in this story too."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A family noticed the grandfather dozing off all day and snoring like a train at night. Everyone joked about it — until we assessed him for sleep apnea.\n\n"
  "With treatment, his daytime sleepiness lifted, his blood pressure settled, and his sugars became easier to control. His whole personality brightened.\n\n"
  "Sometimes the ‘lazy’ or ‘grumpy’ elder is simply exhausted from a treatable condition.\n\n"
  "↗️ Share this with a family that laughs off heavy snoring.",
  "Heavy snoring + daytime sleepiness in a loved one? It’s worth assessing 👉 {{EKACARE_LINK}}",
  "HARD (Book)","7:00 PM",
  quote="Sometimes the ‘lazy’ or ‘grumpy’ elder is simply exhausted from a treatable condition. Snoring is worth taking seriously."),

P("Support Sunday","list","Support Sunday","green",
  "Sleep isn’t a luxury — it directly affects sugar, weight and mood. A household that sleeps better manages diabetes better. This Sunday, set a family wind-down:\n\n"
  "• A fixed ‘screens off’ time for everyone\n"
  "• No heavy meals late at night\n"
  "• Dim lights, quieter home, an hour before bed\n"
  "• Same wake-up time, even weekends\n\n"
  "Better sleep steadies sugar the next day — for everyone.\n\n"
  "🔖 Save this and pick your household’s wind-down time.",
  "Poor sleep worsening a loved one’s sugar? Let’s look at the whole picture 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="A household wind-down for better sugar",
  lines=["A fixed ‘screens off’ time for all","No heavy meals late at night",
         "Dim lights, quiet home before bed","Same wake-up time, even weekends","Better sleep = steadier sugar"]),

# Week 9 (Days 57-60)
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“Diabetes only happens to old people.” Not anymore — and this myth delays diagnosis in the young.\n\n"
  "The truth: type 2 diabetes is rising fast in people in their 20s, 30s and 40s, driven by lifestyle, stress and genetics — and South Asians are at higher risk younger. Even children are being diagnosed.\n\n"
  "Young + busy is exactly when screening gets skipped.\n\n"
  "↗️ Share this with a younger family member who thinks they’re ‘too young’ to check.",
  "Have a younger loved one with risk factors? A simple screen brings peace of mind 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Diabetes only happens to old people.”",
  fact="Type 2 diabetes is rising fast in people in their 20s–40s — and South Asians are at higher risk younger. ‘Too young to check’ is exactly when it gets missed."),

P("Plate & Portion","list","On Your Plate","green",
  "The humble cup of chai/coffee can carry a surprising sugar load across a day — 4 cups at 2 spoons each adds up fast. Gentle ways to cut it:\n\n"
  "• Step down slowly: 2 spoons → 1½ → 1\n"
  "• Try it with less sugar but more elaichi/ginger for flavour\n"
  "• Watch the ‘extra’ cups offered to guests\n"
  "• Beware sweet biscuits that ride along with tea\n\n"
  "Taste buds adjust in a couple of weeks.\n\n"
  "🔖 Save this and start the step-down today.",
  "Want a simple plan to cut hidden sugar for your loved one? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","9:00 AM",
  headline="The hidden sugar in daily chai",
  lines=["Step down slowly: 2 → 1½ → 1 spoon","More elaichi/ginger, less sugar",
         "Watch the ‘extra’ guest cups","Beware biscuits that ride along","Taste buds adjust in ~2 weeks"]),

P("Warning Signs","list","Warning Signs","red",
  "Gums and teeth are an early window into diabetes control that families often overlook:\n\n"
  "• Bleeding, swollen or receding gums\n"
  "• Persistent bad breath\n"
  "• Loose teeth or frequent mouth infections\n"
  "• Slow healing after dental work\n\n"
  "High sugar feeds gum disease, and gum disease worsens sugar — a two-way street. A dental check is part of diabetes care.\n\n"
  "If a loved one has ongoing gum trouble, mention it at their next review.",
  HARD,"HARD (Book)","7:30 PM",
  headline="The mouth signals sugar trouble",
  lines=["Bleeding, swollen or receding gums","Persistent bad breath",
         "Loose teeth / frequent mouth infections","Slow healing after dental work","High sugar and gum disease feed each other"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“Is intermittent fasting safe for my diabetic parent?” A popular question that needs a careful answer.\n\n"
  "For some it can help; for others — especially those on insulin or certain tablets — long gaps risk dangerous lows. It’s not one-size-fits-all.\n\n"
  "• Never start fasting without reviewing their medicines first\n"
  "• Doses often need adjusting on fasting days\n"
  "• Elderly, frail or unstable patients need extra caution\n\n"
  "💬 Thinking about fasting for a loved one? Ask before they start.",
  "Planning fasting (health or festival) for a loved one on medicines? Let’s adjust it safely 👉 {{EKACARE_LINK}}",
  "HARD (Book)","8:00 PM",
  headline="Is intermittent fasting safe for diabetics?",
  lines=["Helps some; risky for others","On insulin/certain tablets: risk of lows",
         "Never start without reviewing medicines","Doses often need adjusting","Elderly/frail need extra caution"]),
]

# ============================ MONTH 3 (Days 61-90) ============================
POSTS += [
# Week 9 continued fits; start Week 10
P("Caregiver Care","quote","For the Caregiver","amber",
  "Managing appointments, reports, refills and receipts is a full-time admin job layered on top of love. No wonder it feels heavy.\n\n"
  "One simple system helps: a single folder (paper or phone) with reports newest-on-top, a note of the next appointment, and a running medicine list. When it’s all in one place, your mind can finally rest a little.\n\n"
  "Organised care is lighter care.\n\n"
  "💬 What’s your system? Share a tip that helps you below.",
  "Want us to help set up a simple records + follow-up plan for your loved one? Ask 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="Organised care is lighter care. One folder, newest report on top, next appointment noted — and your mind can finally rest a little."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A daughter feared her mother’s numbness would lead to the wound she’d read about. So she started a simple weekly foot check.\n\n"
  "One evening she found a small cut the mother hadn’t felt at all. Because it was caught on day one, it healed with basic care — no infection, no hospital, no drama.\n\n"
  "A two-minute habit quietly prevented a crisis. That’s the power of the ordinary check.\n\n"
  "🔖 Save this and start the weekly foot check tonight.",
  "Want to learn the right way to check and care for diabetic feet? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","7:00 PM",
  quote="A two-minute weekly foot check found a cut she never felt — and quietly prevented a crisis. The ordinary habit is the powerful one."),

P("Support Sunday","list","Support Sunday","green",
  "Regular check-ups feel easy to postpone when a loved one ‘feels fine’. Families can make follow-ups a gentle habit, not a fight:\n\n"
  "• Book the next visit before leaving the current one\n"
  "• Tie reviews to a fixed month (birthday, festival)\n"
  "• Prep questions together beforehand\n"
  "• Go along when you can — two sets of ears\n\n"
  "Consistent follow-up is where good control is quietly built.\n\n"
  "🔖 Save this and diarise the next review now.",
  "Due for a review? Booking the next visit is the easiest health decision you’ll make 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="Make check-ups a gentle habit",
  lines=["Book the next visit before leaving","Tie reviews to a fixed month",
         "Prep questions together beforehand","Go along — two sets of ears","Follow-up is where control is built"]),

# Week 11
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“Karela juice / home remedies alone can cure diabetes.” This hope, misused, can be dangerous.\n\n"
  "The truth: some foods may modestly help, but nothing replaces proven treatment. Relying on remedies alone — and quietly stopping medicines — lets sugars climb and complications build silently.\n\n"
  "Use good food WITH your treatment, never instead of it.\n\n"
  "↗️ Share this with a relative swapping medicines for juices.",
  "Wondering what actually helps vs what’s hype for a loved one? Let’s sort fact from fad 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Home remedies alone can cure diabetes.”",
  fact="Some foods help modestly, but nothing replaces proven treatment. Remedies instead of medicines let sugars climb silently. Use good food WITH treatment, not instead."),

P("Plate & Portion","list","On Your Plate","green",
  "Protein is the quietly neglected part of an Indian plate — and it matters hugely for older adults and anyone managing sugar or weight. It keeps them full, steadies sugar, and protects muscle.\n\n"
  "Easy family sources:\n"
  "• Dal, rajma, chana, sprouts\n"
  "• Eggs, curd, paneer, milk\n"
  "• Chicken, fish for non-vegetarians\n"
  "• A handful of nuts as a snack\n\n"
  "Aim for some protein in every meal, not just dinner.\n\n"
  "🔖 Save this and add one protein to breakfast tomorrow.",
  "Want a protein target suited to a loved one’s age and kidneys? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","12:30 PM",
  headline="Don’t forget the protein",
  lines=["Dal, rajma, chana, sprouts","Eggs, curd, paneer, milk",
         "Chicken, fish for non-veg","A handful of nuts as a snack","Some protein in EVERY meal"]),

P("Warning Signs","list","Warning Signs","red",
  "Uncontrolled diabetes and obesity raise heart risk quietly. Some heart warning signs show up differently — especially in women and the elderly:\n\n"
  "• Breathlessness on mild effort\n"
  "• Unusual fatigue or sweating\n"
  "• Discomfort in chest, jaw, back or left arm\n"
  "• Swelling in the legs\n\n"
  "These deserve urgent attention — never a ‘let’s see tomorrow’.\n\n"
  "If a loved one has these, please don’t delay medical help.",
  HARD,"HARD (Book)","7:30 PM",
  headline="Heart signs families miss",
  lines=["Breathlessness on mild effort","Unusual fatigue or sweating",
         "Discomfort in chest, jaw, back or arm","Swelling in the legs","Urgent — never ‘see tomorrow’"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“What vaccines does a diabetic actually need?” A great, often-missed question.\n\n"
  "Diabetes can weaken defences against certain infections, so a few vaccines matter more:\n"
  "• Yearly flu vaccine\n"
  "• Pneumonia (pneumococcal) vaccine\n"
  "• Others your doctor may advise by age/history\n\n"
  "Prevention is far kinder than treating an infection that spikes their sugar.\n\n"
  "💬 Does your loved one get the yearly flu shot? Ask below if they should.",
  "Want to know which vaccines suit your loved one? We’ll advise at a consult 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="Which vaccines do diabetics need?",
  lines=["Diabetes can weaken infection defences","Yearly flu vaccine",
         "Pneumonia (pneumococcal) vaccine","Others by age/history","Prevention beats a sugar-spiking illness"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "Patience runs out. You’ll snap, sigh, feel resentful — and then feel guilty for feeling it. That doesn’t make you a bad caregiver. It makes you human and tired.\n\n"
  "Give yourself the grace you so freely give your loved one. Step away for five minutes when it’s too much. Forgive yourself for the hard moments. Then come back.\n\n"
  "Caring for someone for years is a marathon, not a test of sainthood.\n\n"
  "💬 Send a 🤍 if you needed to hear this today.",
  "Carrying a loved one’s care alone and feeling stretched? Let us share the load 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="Caring for someone for years is a marathon, not a test of sainthood. Give yourself the grace you so freely give them."),

P("Small Wins / Story","quote","A Real Story","teal",
  "After menopause, a woman watched her weight creep up and her sugars follow — and blamed herself. In truth, hormones had shifted the whole game.\n\n"
  "We adjusted her food, added strength work and protected her sleep — no crash dieting. Over months her weight eased down and her sugars steadied. Understanding the ‘why’ replaced the shame with a plan.\n\n"
  "Sometimes the missing ingredient isn’t willpower — it’s the right explanation.\n\n"
  "↗️ Share this with a woman who’s blaming herself.",
  "Weight or sugar changing around menopause for a loved one? There’s real help 👉 {{EKACARE_LINK}}",
  "Soft (Share)","7:00 PM",
  quote="Sometimes the missing ingredient isn’t willpower — it’s the right explanation. Understanding the ‘why’ replaces shame with a plan."),

P("Support Sunday","list","Support Sunday","green",
  "Setbacks happen — a bad report, a festival binge, a missed month of walks. How the family reacts decides whether a loved one gives up or gets back up.\n\n"
  "• Respond with support, not ‘I told you so’\n"
  "• Treat a slip as data, not a disaster\n"
  "• Restart the very next meal — no waiting for Monday\n"
  "• Celebrate the return, not just the streak\n\n"
  "Progress is never a straight line. Compassion keeps it moving.\n\n"
  "🔖 Save this for the next tough week.",
  "Had a setback with a loved one’s control? Let’s reset the plan together 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="Handling setbacks with compassion",
  lines=["Support, not ‘I told you so’","Treat a slip as data, not disaster",
         "Restart the very next meal","Celebrate the return, not just the streak","Progress is never a straight line"]),

# Week 12
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“Once you’re fat, you’re always fat — metabolism is destiny.” This belief kills motivation before anyone begins.\n\n"
  "The truth: metabolism is influenced by muscle, activity, sleep and food — much of which can change. Progress may be slower for some, but ‘impossible’ is a myth. Bodies respond, at any age.\n\n"
  "The goal isn’t a magazine body — it’s better health and mobility.\n\n"
  "↗️ Share this with someone who’s decided change is impossible.",
  "Want a realistic, sustainable plan for a loved one’s weight? We build those 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Once fat, always fat — metabolism is destiny.”",
  fact="Metabolism is influenced by muscle, activity, sleep and food — much of which can change. Slower for some, but ‘impossible’ is a myth. Bodies respond at any age."),

P("Plate & Portion","list","On Your Plate","green",
  "Sweet drinks are one of the fastest ways to spike sugar — and the easiest to overlook because they don’t feel like ‘food’. Help the whole family rethink the glass:\n\n"
  "• Swap soft drinks & packaged juice for water, chaas, nimbu paani (no sugar)\n"
  "• Beware ‘health’ drinks and sweetened lassi\n"
  "• Keep a jug of infused water (mint, lemon) in the fridge\n"
  "• Save sweet drinks for rare occasions\n\n"
  "You can drink a lot of sugar without noticing.\n\n"
  "🔖 Save this and restock the fridge today.",
  "Want the hidden liquid sugar in your family’s day mapped out? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","12:30 PM",
  headline="Rethink the glass, not just the plate",
  lines=["Swap soft drinks/juice for water, chaas","Beware ‘health’ drinks & sweet lassi",
         "Keep infused water (mint, lemon) ready","Save sweet drinks for rare occasions","You can drink a lot of sugar unnoticed"]),

P("Warning Signs","list","Warning Signs","red",
  "Living with a long-term condition takes a mental toll that families often miss. Low mood and depression are common — and they quietly worsen sugar control too.\n\n"
  "Watch for a loved one:\n"
  "• Losing interest in things they enjoyed\n"
  "• Sleeping or eating much more or less\n"
  "• Withdrawing, irritable, or hopeless\n"
  "• Neglecting their medicines and self-care\n\n"
  "Emotional health is part of diabetes care — not separate from it.\n\n"
  "If this sounds like someone you love, please reach out for support.",
  HARD,"HARD (Book)","7:30 PM",
  headline="The mental toll of chronic illness",
  lines=["Losing interest in things they enjoyed","Sleeping/eating much more or less",
         "Withdrawing, irritable or hopeless","Neglecting medicines & self-care","Emotional health is part of diabetes care"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“What waist size should I actually worry about?” A more useful number than weight alone.\n\n"
  "For South Asian adults, raised risk generally starts around:\n"
  "• Men: waist over ~90 cm (about 36 inches)\n"
  "• Women: waist over ~80 cm (about 32 inches)\n\n"
  "Belly fat is more telling than the scale — a ‘normal weight’ person with a large waist still carries risk.\n\n"
  "💬 Measure a loved one’s waist this week — snug, at the navel. Surprised? Tell me below.",
  "Want a full risk check for a loved one — not just weight? Book a consult 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="What waist size to worry about",
  lines=["Belly fat tells more than the scale","Men: over ~90 cm (36 in) = raised risk",
         "Women: over ~80 cm (32 in) = raised risk","Measure snug, at the navel","‘Normal weight’ + big waist still = risk"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "You don’t have to carry this alone — and yet so many caregivers do, quietly, until they’re running on empty.\n\n"
  "Build a small circle: a sibling who handles refills, a neighbour who checks in, a friend who just listens. Asking for help isn’t weakness — it’s how caregiving stays sustainable for the long haul.\n\n"
  "The strongest caregivers aren’t the ones who do everything — they’re the ones who let others in.\n\n"
  "💬 Tag or thank someone who helps you care. Let’s see those circles.",
  "Want your loved one’s care plan simplified so it’s easier to share with family? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="The strongest caregivers aren’t the ones who do everything — they’re the ones who let others in. Asking for help isn’t weakness."),

P("Small Wins / Story","quote","A Real Story","teal",
  "The change I remember most wasn’t a number — it was a photo. A family sent me a picture of all three generations walking together in the park after dinner, something they’d started six months earlier ‘for Papa’s sugar’.\n\n"
  "Papa’s HbA1c had improved. But so had everyone’s energy, their evenings, their closeness. One person’s diagnosis had quietly made the whole family healthier.\n\n"
  "Care given together comes back to everyone.\n\n"
  "🔖 Save this and start your family’s walk tonight.",
  "Want a plan the whole family can rally around? That’s exactly how we work 👉 {{EKACARE_LINK}}",
  "Soft (Save)","7:00 PM",
  quote="One person’s diagnosis quietly made the whole family healthier. Care given together comes back to everyone."),

P("Support Sunday","list","Support Sunday","green",
  "Milestones deserve to be seen. When a loved one sticks with change, celebrating it fuels the next month. This Sunday, notice the wins:\n\n"
  "• A better report — say it out loud\n"
  "• 30 days of walks — mark it together\n"
  "• A dose reduced by the doctor — that’s a team win\n"
  "• Smaller wins too: more energy, better sleep\n\n"
  "What gets celebrated gets repeated.\n\n"
  "🔖 Save this and celebrate one win with your loved one today.",
  "Reached a milestone and want to build on it? Let’s plan the next step 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="Celebrate the milestones",
  lines=["A better report — say it out loud","30 days of walks — mark it together",
         "A dose reduced — a team win","Notice energy & sleep improving","What gets celebrated gets repeated"]),

# Week 13 (Days 88-90)
P("Myth vs Fact","myth","Myth vs Fact","teal",
  "“Walking is enough — no need for tests or medicines.” Walking is wonderful, but this myth can hide a rising problem.\n\n"
  "The truth: activity is powerful, yet some people still need medicines and regular monitoring to stay safe. You can’t feel your HbA1c or your kidney function — only testing shows them.\n\n"
  "Do the walk AND the check-ups. They work best together.\n\n"
  "↗️ Share this with someone relying on walking alone.",
  "Want to know if a loved one’s current plan is truly enough? A review will tell 👉 {{EKACARE_LINK}}",
  "Soft (Share)","8:30 AM",
  myth="“Walking is enough — no need for tests or medicines.”",
  fact="Activity is powerful, but some still need medicines and monitoring. You can’t feel your HbA1c or kidney function — only testing shows them. Do both."),

P("Plate & Portion","list","On Your Plate","green",
  "Ninety days of small changes, distilled into one save-worthy card. If your family keeps just these, you’ve done the important work:\n\n"
  "• ½ plate veg, ¼ protein, ¼ carbs — veg first\n"
  "• Swaps beat bans; drink your water, not your sugar\n"
  "• A 10-minute family walk after dinner\n"
  "• Weekly foot check; yearly eye check\n"
  "• Know the next HbA1c date; keep one reports folder\n"
  "• Support beats supervision — always\n\n"
  "🔖 Save this. ↗️ Share it with a caregiver who needs it.",
  "Ready to turn 90 days of habits into a plan built for your loved one? We’re here 👉 {{EKACARE_LINK}}",
  "Soft (Save/Share)","12:30 PM",
  headline="Your 90-day family cheat sheet",
  lines=["½ veg, ¼ protein, ¼ carbs — veg first","Swaps beat bans; drink water not sugar",
         "10-minute family walk after dinner","Weekly foot check; yearly eye check","Know the next HbA1c; one reports folder"]),

P("Warning Signs","list","Warning Signs","red",
  "Before we start the next cycle, here’s the caregiver’s at-a-glance list — the signs that always deserve a doctor’s attention, not a wait-and-watch:\n\n"
  "• A wound not healing, or a hot, swollen foot\n"
  "• Frequent lows (sweating, shaking, confusion)\n"
  "• Vomiting with drowsiness or fast breathing\n"
  "• New chest pain or breathlessness\n"
  "• Sudden vision change\n\n"
  "Save this where the family can see it.\n\n"
  "When in doubt, it’s always okay to get them checked.",
  HARD,"HARD (Book)","7:30 PM",
  headline="The ‘always get checked’ list",
  lines=["A non-healing wound / hot swollen foot","Frequent lows: sweating, shaking, confusion",
         "Vomiting with drowsiness / fast breathing","New chest pain or breathlessness","Sudden vision change"]),
]

# ============================ FILLERS to reach 90 (weekday-aligned by builder) ============================
POSTS += [
P("Warning Signs","list","Warning Signs","red",
  "Poor circulation in the legs is a quiet danger in long-standing diabetes. Families can spot early clues a loved one may ignore:\n\n"
  "• Cold or pale feet, even in warm weather\n"
  "• Cramping pain in the calves when walking, easing on rest\n"
  "• Skin colour changes; hair loss on the legs\n"
  "• Slow-healing sores on the lower legs or feet\n\n"
  "Good circulation protects the feet — this deserves a proper check, not a shrug.\n\n"
  "If a loved one has cold feet or walking cramps, please get it assessed.",
  HARD,"HARD (Book)","7:30 PM",
  headline="Poor leg circulation: the quiet danger",
  lines=["Cold or pale feet, even when warm","Calf cramps on walking, easing on rest",
         "Skin colour changes; leg hair loss","Slow-healing sores on the legs","Good circulation protects the feet"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“How much water should a diabetic actually drink?” A simple question that matters more than families realise.\n\n"
  "Good hydration helps the body flush excess sugar and protects the kidneys. For most adults, aim for steady water through the day — roughly 8 glasses unless the doctor has advised a limit (some heart/kidney patients need less).\n\n"
  "• Water, chaas and nimbu paani (no sugar) count\n"
  "• Increased thirst can itself signal high sugar — worth checking\n\n"
  "💬 Does your loved one drink enough water? Ask below.",
  "Not sure how much fluid is right for a loved one’s heart/kidneys? We’ll advise 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="How much water should they drink?",
  lines=["Hydration helps flush sugar, protects kidneys","Aim for steady water through the day",
         "~8 glasses unless advised otherwise","Water, chaas, nimbu paani (no sugar) count","Extra thirst can itself signal high sugar"]),

P("Ask the Doctor","list","Ask the Doctor","teal",
  "“Can stress really raise blood sugar?” Yes — and it’s one of the most overlooked pieces.\n\n"
  "Stress hormones push sugar up, disturb sleep, and drive comfort eating. A loved one doing ‘everything right’ can still see high numbers during a stressful stretch.\n\n"
  "• Notice work, grief and worry as real factors\n"
  "• Gentle routine, walks and sleep genuinely help\n"
  "• Don’t just blame the food when life is hard\n\n"
  "💬 Have you seen a loved one’s sugar rise during a stressful time? Share below.",
  "Stress worsening a loved one’s control? Let’s look at the whole picture 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","8:00 PM",
  headline="Can stress raise blood sugar?",
  lines=["Yes — stress hormones push sugar up","It disturbs sleep and drives comfort eating",
         "‘Doing everything right’ can still spike","Routine, walks and sleep genuinely help","Don’t only blame the food"]),

P("Caregiver Care","quote","For the Caregiver","amber",
  "Caring from another city carries its own ache — the worry between phone calls, the guilt of distance, the helplessness when something goes wrong.\n\n"
  "You can still care powerfully from afar: set up their medicines and refills online, build a local check-in (neighbour, relative), keep one shared record you can both see, and join their doctor visits by call when allowed.\n\n"
  "Distance changes how you care — not how much.\n\n"
  "💬 Caring long-distance? Send a 🤍 — this one’s for you.",
  "Want help setting up a loved one’s care so you can support from anywhere? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="Distance changes how you care — not how much. You can still care powerfully from another city."),

P("Caregiver Care","quote","For the Caregiver","amber",
  "It stings when the caregiving falls on one person while others stay distant. Resentment builds quietly, and it’s exhausting to carry both the care and the unfairness.\n\n"
  "Where you can: ask for specific help, not general (‘can you handle the monthly refills?’ lands better than ‘help more’). Share the record so no one’s in the dark. And protect yourself from bitterness — for your own sake.\n\n"
  "You didn’t sign up alone, even if it feels that way.\n\n"
  "💬 If this is your reality, you’re seen. Drop a 💙.",
  "Want a shareable care plan that makes it easier for family to pitch in? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Comment)","9:00 PM",
  quote="Ask for specific help, not general — ‘can you handle the refills?’ lands better than ‘help more’. You didn’t sign up alone."),

P("Small Wins / Story","quote","A Real Story","teal",
  "A man drank six sugary teas a day and swore it made no difference. As an experiment, he cut to two — same food otherwise.\n\n"
  "Within weeks his afternoon energy stopped crashing, his fasting sugar eased, and he was sleeping better. He was stunned that something so small moved the needle.\n\n"
  "Sometimes the biggest win is hiding in the smallest daily habit.\n\n"
  "🔖 Save this and pick one small daily habit to test for two weeks.",
  "Want help spotting your loved one’s ‘small habit, big impact’ change? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","7:00 PM",
  quote="Sometimes the biggest win is hiding in the smallest daily habit — like six sugary teas becoming two."),

P("Small Wins / Story","quote","A Real Story","teal",
  "The patient I’m proudest of didn’t do anything dramatic. No crash diet, no miracle. She simply kept her small habits going — week after week, through festivals, illnesses and dull days — for a whole year.\n\n"
  "Her reports at twelve months looked like a different person’s. Consistency, not intensity, rewrote her health.\n\n"
  "The families who win aren’t the fastest. They’re the ones who don’t quit.\n\n"
  "🔖 Save this for the weeks when motivation runs low.",
  "Want a plan built for the long haul, not a crash? That’s how we work 👉 {{EKACARE_LINK}}",
  "Soft (Save)","7:00 PM",
  quote="The families who win aren’t the fastest — they’re the ones who don’t quit. Consistency, not intensity, rewrites health."),

P("Support Sunday","list","Support Sunday","green",
  "Movement sticks when it’s fun, not a chore. The families who stay active turned it into something they enjoy together. This Sunday, make it playful:\n\n"
  "• Bring back a sport — badminton, cricket, cycling\n"
  "• Dance to a few songs after dinner\n"
  "• Turn errands into walks; park further away\n"
  "• Make it social — walk with friends or neighbours\n\n"
  "The best exercise is the one your loved one looks forward to.\n\n"
  "🔖 Save this and plan one fun-active thing this week.",
  "Want activity ideas safe for a loved one’s joints and heart? Ask us 👉 {{EKACARE_LINK}}",
  "Soft (Save)","11:00 AM",
  headline="Make movement fun for everyone",
  lines=["Bring back a sport: badminton, cricket, cycling","Dance to a few songs after dinner",
         "Turn errands into walks; park further","Make it social — friends & neighbours","The best exercise is one they enjoy"]),
]

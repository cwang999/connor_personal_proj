{% include navbar.html %}

# Tech Talk 0 Key Learnings
Difference between static coding and dynamic structures (we want data structures)’
- Dictionaries are dynamic structures
- Try Except Else - tries to open files/complete task; if fails, goes to except; if no errors, goes to else block

# TPT 0.1 Beneficial and Harmful Effects of Computing
- Drones Good and bad May violate privacy, but useful for search and rescue, photography, etc. 
- Dopamine - Gaming, social media, instagram, youtube gets in the way of life
- Phone trees - saves money, reduces hold time, but may be inaccurate
  - Can be represented with code: if statements, sequencing, and procedures
- Come up with 3 beneficial and harmful effects of computing. Then talk about dopamine issues above. Real? Anything impacting success?
  - Action: Instagram algorithms collect data about your preferences, creating a customized profile suited to your tastes. However, this could be harmful because it could cause privacy concerns. Phones and texting help us communicate when we’re far away from each other. However, reliance on this form of communication breaks down personal interaction. We’ve come to depend on things like Wifi, internet access, and online services, which help us in our daily lives. However, we have become overly reliant on them and become lazy.

# TPT 0.2 Digital Divide 
- Have or don’t have in relation to computers, internet, and technology
- Poorer, rural areas might have less access to technology, or some countries have restricted internet access 
- Contributing factors: socioeconomic, geographic, demographic
- Action: Answer the following How does someone empower themselves in a digital world? 
  - We can use digital technology like the internet by finding resources to help them with education or finding career opportunities How does someone that is empowered help someone that is not empowered? People with access to resources should share them with those who have little access to computers and technology. Ex: if you’re replacing your old laptop with a new one, donate the old one to someone who needs it.
- Describe something you could do at Del Norte HS
  - The school already hands out chromebooks to students who don’t have a computer. However, a lot of divide exists because some students aren’t familiar with technical and/or social media, and helping students move onto these platforms can increase connectivity and communication.
- Is paper or red tape blocking digital empowerment? Are there such barriers at Del Norte
  - Any form of restricting access to technology is not digital empowerment. One example is the PUSD wifi, which isn’t great and lots of websites are restricted. Websites that would greatly benefit students’ learnings are prohibited.

# Tech Talk 1 Key Learnings
TT1
- Lists and dictionaries are collection data structures (hold multiple values)
- CRUD: user defines table as a class
  - A list is a class structure
  - Ex: infoDb = [] is an object of class list
  - Classes: attributes and methods (functions)
    - Methods apply to all objects
    - Call method with a dot method
    - Ex: infoDb.append(--{insert dictionary w/ key value paris}--)
Try to print info from lists using for, while loop
While uses boolean condition
For takes care of the counter by itself, don’t need to add 1 (increment) each time
Factorials can use recursion
In a while loop, need exit condition
  - Ex: n = 1 or n = 0, return 1
For fibonacci challenge, use try except (can’t use negative numbers in fibonacci)

# 5.3 Computer Bias
5.3 Computer Bias
Computer algorithms and programs may have unintentional bias, possibly due to the data they collect that is unrepresentative of different genders, races etc.
- HP computer facial recognition software
Computer bias is sometimes beneficial, ex targeted ads
Watch the video... HP computers are racist
Come up with some thoughts on the video and be ready to discuss them as I call on you. Here are some ideas...
- Does the owner of the computer think this was intentional?
  - Yes, it seems the owner thinks this was intentional racism by HP computers.
- If yes or no, justify your conclusion.
  - The owner openly stated that he thinks HP computers are racist. However, this is probably unintentional computing bias.
- How do you think this happened?
  - When HP was testing their computers, they probably took data from a group of individuals who weren’t representative of everyone. It was probably unintentional, and their data set probably was mostly light skinned people.
- Is this harmful? Was it intended to be harmful or exclude?
  - This may be harmful because it excludes darker skinned people but it wasn’t intentional. It just so happened that they overlooked how their data set was not representative.
- Should it be corrected?
  - Yes, in cases of computing bias that adversely and unintentionally affects certain groups, the bias should be corrected.
- What would you or should you do to produce a better outcome?
  - In order to avoid this bias, you should find representative data samples when developing computer programs that represent the wider population who will use your software.

# 5.4 Crowdsourcing
- Way to reduce bias in computing
- Example: Wikipedia: often inaccurate, but often corrected through self-policing
- Data samples must be representative of larger population
- Actions
  - CompSci has 150 principles students. Describe a crowdsource idea and how you might initiate it in our environment?
    - One crowdsource idea is that we could collect data about what CSP students think would be the best way to learn computer science. This would be like the surveys done by AP statistics students. We could then learn from this feedback and adjust the CSP curriculum by, for example, changing the focus from PBL to a more traditional learning style if students struggle with the former.
  - What about Del Norte crowdsourcing? Could your final project be better with crowdsourcing?
    - Del crowd sourcing is regularly done with AP Stats student surveys and the regular DNN videos in which some students go around interviewing people on campus. My final project could be better with crowdsourcing because I could be getting feedback about my program from Del Norte students.

# 5.5 Legal and Ethical Concerns
- Royalties: companies can make money on patents, ex: Qualcomm
- If you use GPL version 3 and distribute that software, that software must be open source and free
- Qualcomm doesn’t want them to be free, wants patents (Patents vs GPL)
- Qualcomm uses GPL too
- Always abide by license terms
Actions:
- When you create a GitHub repository it requests a license type. Review the license types in relationship to this Tech Talk and make some notes in GitHub pages.
- The licenses I found include Apache License 2.0, GNU General Public License v3, MIT License, Creative Commons Zero v1 Universal, etc.
- Apache: 
- Permissions: commercial use, modification, distribution, patent use, private use
- Limitations: trademark use, liability, warranty
- GNU: 
  - Permissions: Commercial use, modification, distribution, patent use, private use
  - Limitations: Liability, warranty
- MIT:
  - Commercial use, modification, distribution, private use
  - Limitations: Liability, warranty
- Make a license for your personal and Team project. Document license you picked and why.
  - I chose the GNU General Public License v3 for both my personal and team project because I felt it gives the most freedom to the user to distribute and modify the software. I have no incentive to make it closed source/non-removable.

# 5.6 Github Actions
- Avoid giving out personal information (phone number, credit card number, etc.)
- Some things known by everyone (city, email, etc.)
- Good practices:
  - Multi Factor authentication
  - Beware of malware in email attachments
- Watch 5.6 Video 2
  - Authentication measure protect devices and information from unauthorized information
  - Types of authentiation: what you know, what you want, what you have
  - Viruses are malicious programs that can copy themselves and gain access to systems that they are not supposed to be in
  - Virus scans can help prevent malicious code from damaging system 
  - Once legitimate access to a system is gained, it's important to ensure data sent to/from system is uncompromised - encryption and decryption (prevent unauthorized interception of data)
  - Encryption: symmetric and asymmetric
    - Asymmetric: public key encription - uses two keys, a public for encrypting and a private for decrypting; anyone can encrypt but private key needed for decrypting
    - Digital certificates: certificate authorities issue digital certificates that validate the ownership of encryption keys used in secure communications
- Actions
  - Describe PII you have seen on project in CompSci Principles.
    - PII includes our login information that we use on Slack and Github. Besides that, we don’t usually use risky PII in CSP.
  - What are your feelings about PII and your exposure?
    - I try to make strong passwords but other than that I don’t think too much about security, which I know I should think more about. 
  - Describe good and bad passwords? What is another step that is used to assist in authentication.
    - Good password = many types of characters, good length. Bad = too simple and predictable. Multi-factor authentication (like code sent to the phone) is used to help authentication.
  - Try to describe Symmetric and Asymmetric encryption.
    - Symmetric encryption uses the same publicly available key to encrypt and decrypt. Asymmetric encryption uses a public key to encrypt and a private key to decrypt. 
  - Provide an example of encryption we used in deployment.
    - I was not a deployment manager for my project, so I don’t know the details of encryption, but it was likely used to make our website’s address more secure.
  - Describe a phishing scheme you have learned about the hard way. Describe some other phishing techniques.
    - Fortunately I haven’t been a victim of phishing yet as I am careful not to click suspicious links. Phishing techniques usually involve suspicious emails that mimic major organizations to try to get you to provide personal information.

# Tech Talk 2 Key Learnings
- Keep your files organized
- Don’t keep everything in the root
- When you have both procedural and data abstraction, that’s a class
- Learn how to debug code in IntelliJ

# WEEK 5 Study Plan
Work on corrections on Wednesday and Friday and update Github Page. It seems I still have to study more about the internet terminology (like protocols, TCP IP, etc.). Beyond this area of weakness, I mostly understand the other topics because they are conceptually intuitive and my ability ot answer the question depends on thinking clearly and reading the problem thoroughly. I will continue to work on these areas as the week progresses.

# Mock Test 1 Corrections
(1) A programmer is writing a program that is intended to be able to process large amounts of data. Which of the following considerations is LEAST likely to affect the ability of the program to process larger data sets?
The answer is B: how many programming statements the program contains. The efficiencey and speed of the program does not depend on the number of code statements. I selected A, or how long the program takes to run. This is incorrect (it DOES affect the efficency) because longer times means lower efficiency.

(9) Of the following potential benefits, which is LEAST likely to be provided by the upgraded system?
The answer is not A because the diagram shows humans will still be needed for some inquiries. The answer is B, the company will be able to provide a human representative for any incoming call because this is impossible after business hours.

(23) Which of the following has the greatest potential for compromising a user’s personal privacy?
The answer is no B, or IP address, because it is needed for sending and receiving info on the internet and doesn't contain extra about the user. Browser cookes (A) can be used to track/collect user info.

(29) In order to test the program, the programmer initializes numList to [0, 1, 4, 5]. The program displays 10, and the programmer concludes that the program works as intended. Which of the following is true?
The answer is not D, that the test only shows the program works for increasing order. This is wrong because the "for each" block means the first value is added twice. This means that the answer is C; it is insufficent to prove the program works for all cases.

(38) When a cellular telephone user places a call, the carrier transmits the caller’s voice as well as the voice of the person who is called. The encoded voices are the data of the call. In addition to transmitting the data, the carrier also stores metadata. The metadata of the call include information such as the time the call is placed and the phone numbers of both participants. For which of the following goals would it be more useful to computationally analyze the metadata instead of the data?
The answer is C, both II and III, because in addition to providing info about the time calls were made, the metadata also includes phone numbers of both participants, so it can be used to see who was in contact with criminals and thus generate a list of suspects.

# Mock Test 2 Corrections
N/A - Score 50/50


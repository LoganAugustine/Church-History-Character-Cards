# Church History Character Cards

I'm currently taking Church History (HT5101, The Church to the Modern Era @ Dallas Theological Seminary) and I'm amazed by how many people have come before us in our faith! So many of them have made such a tremendous impact (for better or for worse) in Christian history. And at the same time, it seems impossible to know enough about all of them. 

So I've made it my goal to provide a resource to myself (and to whoever reads this) for easy access to important facts in church history characters. Their pertanent information is listed on a playing card (a lot like a Pokemon card) for easy access and memorization. 

## The Data 

Each person and the notes I've included for them are collected from my notes on Church History. This class has been taught by Dr. John D. Hannah and much of the information is from his lectures and his textbook, "Invitation to Church History: World." If you have any additions or disagreements with the information presented, feel free to make a copy and edit them, or message me! And please also know, this is a work in progress. Not everything on here is finished, and I certainly could've overlooked many details! So let me know. 

The data I collected can be found in the People_Profiles.csv. Trust me, it looks a lot nicer on my Google Doc and Google Sheet. The categories I chose to include are Name, Date, Era, Location, Nickname, Quote, Writings, Context/Controversies, Opponents, Other Info, Most Well Known For, and Strengths/Weaknesses. So far thats been enough for me! 

## The Code

I still update these databases periodically (they are my notes in class, after all), so don't expect everything to be complete. Then I export the Google Sheet as a CSV and place it where my Python code can access it. 

The Python script was largely created usign AI (I'm proficient in Python, but had never used the Pillow Package for .png drawing. You can judge me all you want.) So first off, make sure to install the Pillow Package (PIL). The code calls 2 files: 
1. People_Profiles.csv (mentioned above)
2. card_background.png
The card background is also generated using AI, but you can pick any background you'd like. In the future, I'd love to add famous images of theologians to these cards, but I don't have time for that now!

Once everything is set up, you can run the code and it will create a folder of png's for each character in your directory! Hope you enjoy!

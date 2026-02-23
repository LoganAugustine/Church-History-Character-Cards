# Church History Character Cards

I'm currently taking Church History (HT5101, The Church to the Modern Era @ Dallas Theological Seminary) and I'm amazed by how many people have come before us in our faith! So many of them have made such a tremendous impact (for better or for worse) in Christian history. And at the same time, it seems impossible to know enough about all of them. 

So I've made it my goal to provide a resource to myself (and to whoever reads this) for easy access to important facts in church history characters. Their pertanent information is listed on a playing card (a lot like a Pokemon card) for easy access and memorization. 

## The Data 

Each person and the notes I've included for them are collected from my notes on Church History. This class has been taught by Dr. John D. Hannah and much of the information is from his lectures and his textbook, "Invitation to Church History: World." If you have any additions or disagreements with the information presented, feel free to make a copy and edit them, or message me! And please also know, this is a work in progress. Not everything on here is finished, and I certainly could've overlooked many details! So let me know. 

The data I collected can be found in the Character_Cards_Data.csv. Lucky for you, it looks great on GitHub's CSV viewer! I also included the .xlsx for you if you need. The categories I chose to include are Name, Date, Era, Location, Nickname, Quote, Writings, Context/Controversies, Opponents, Other Info, Most Well Known For, and Strengths/Weaknesses. So far thats been enough for me! 

## The Code

I still update these databases periodically (they are my notes in class, after all), so don't expect everything to be complete. Then I export the Google Sheet as a CSV and place it where my Python code can access it. 

The Python script was largely created usign AI (I'm proficient in Python, but had never used the Pillow Package for .png drawing. You can judge me all you want.) So first off, make sure to install the Pillow Package (PIL). The code calls 2 files: 
1. Character_Cards_Data.csv (mentioned above)
2. card_background.png

The card background is also generated using AI, but you can pick any background you'd like. In the future, I'd love to add famous images of theologians to these cards, but I don't have time for that now!

The unfortunate (but convienient) fact is that each of these cards is essentially hard-coded, with the text being literally drawn onto the .png. This works as long as you keep your cards in the same folder, and the script will simply write over it. I have no clue if this is the best way, but I'm a simple man! 

Once everything is set up, you can run the code and it will create a folder of png's for each character in your directory! Hope you enjoy!

## Examples

See the examples folder for what the output will look like. I would take 1 million years to upload all of the cards onto GitHub, and then I'd get done and want to edit them again. So if you have a creative way for me to display them where I can continually update them, let me know. Otherwise, try it out for yourself!


### To Do List (for me) 
Next steps: 
1. Figure out a way better font than Arial
2. Standardize "Date" and "Location" format
3. Clean up data and continue to evolve content
4. Add different colored cards to indicate the period/era (Yellow for early church, Red for Medieval, etc.)
5. Add images of the Characters to each card. This will take forever...
6. Add an "Importance" rating. There are some who are way more important than others. No offense. 

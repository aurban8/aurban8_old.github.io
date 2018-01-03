Title: Learning R with DataCamp
Date: 2018-01-03 12:01
Category: Blog
Tags: r, rstats, learning, python, online-learning, notecards
Slug: learning-r
Authors: Andrea Urban
Summary: *Learning R with DataCamp's. Comparing R and Python. Pictures of Notecards.*

*Learning R with DataCamp's. Comparing R and Python. Pictures of Notecards.*

I recently worked through [DataCamp’s Introduction to R course](https://www.datacamp.com/courses/free-introduction-to-r){:target="_blank"}. This was my first time typing R code. I’ve seen it before but haven’t really learned too much about it. I made some notes on notecards while I was going through the exercises and I’ll share them below with some of my thoughts. 

<center> ![Notecard1]({filename}/images/r_intro/r_fig1a.JPG)
Notecard #1: My introduction to `<-`   </center> 


Besides the unique way of assigning variables (`<-`) , R seems pretty straightforward. I was curious about why “c” was used to create a vector. Does it stand for “create,” “concatenate,” something else? [Stackoverflow to the rescue!](https://stackoverflow.com/questions/11488820/why-use-c-to-define-vector){:target="_blank"} It looks like “c” stands for combine. The command **combines** single-value vectors into a single vector with multiple values. Ok, got it.

Also, I had a question right from the start about whether there was a print function. It seems like to print the values of a variable, the user just types the variable’s name. That seems simple enough, but I’m still on the lookout for an actual “print” command.  I wonder if it even exists...

<center> ![Notecard2]({filename}/images/r_intro/r_fig1b.JPG)
Notecard #2: Hallelujah! R starts counting with the number 1  </center> 

I am **VERY EXCITED** about indexing starting at 1. **VERY EXCITED!**
I’ve tweeted about this topic more than once.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">There are two kinds of people in the world.<br><br>0) Those who can count.<br><br>1) Those who can&#39;t.<br><br>2) Those who count starting with 0.</p>&mdash; Andrea Urban (@AndreaUrbanPhD) <a href="https://twitter.com/AndreaUrbanPhD/status/870697006309691392?ref_src=twsrc%5Etfw">June 2, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">How *some* programmers count cats: &quot;Let&#39;s see... 0, 1, 2, 3.... Hmm..  This means there are 4 cats.&quot; <a href="https://twitter.com/hashtag/cats?src=hash&amp;ref_src=twsrc%5Etfw">#cats</a> <a href="https://twitter.com/hashtag/counting?src=hash&amp;ref_src=twsrc%5Etfw">#counting</a> <a href="https://twitter.com/hashtag/numbers?src=hash&amp;ref_src=twsrc%5Etfw">#numbers</a></p>&mdash; Andrea Urban (@AndreaUrbanPhD) <a href="https://twitter.com/AndreaUrbanPhD/status/785515478277947392?ref_src=twsrc%5Etfw">October 10, 2016</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



I am also a fan of how selecting parts of a vector includes ALL the digits mentioned in the select statement. In Python, it’s not as clear, at least to me. Here's some Python code to demonstrate this.

    #!python
    # Define a list in python
    x=[1,2,3,4]
    # Return 2nd and 3rd element (Remember python starts numbering at 0.)
    print(X[1:3])
    [2,3]

<center> ![Notecard3]({filename}/images/r_intro/r_fig2a.JPG)
Notecard #3: Matrices   </center> 

It seems like R’s matrices are like numpy arrays, they can only contain data of one type. 

<center> ![Notecard4]({filename}/images/r_intro/r_fig2b.JPG)
Notecard #4: Factors   </center> 

The `factor` type in R is interesting. I can see how this could be very useful when performing statistical operations like chi-square tests.

<center> ![Notecard5]({filename}/images/r_intro/r_fig3a.JPG)
Notecard #5: Dataframes  </center> 

Using `str` to get the “structure of a dataframe seems dangerous because of its similarity to `string`.  Seems like there are other better options for structure. Here are [few](http://www.thesaurus.com/browse/structure){:target="_blank"} I found


<center> ![Synonyms]({filename}/images/r_intro/r_structure_synonyms.png)
Synonyms for "Structure"   </center> 

My suggestion is skeleton! 💀 

`ske()`   

<center> ![Notecard6]({filename}/images/r_intro/r_fig3b.JPG)
Notecard #6: Lists  </center> 

In this course, I learned about the various data structures in R: vectors, matrices, factors, dataframes, and lists.

I was not a fan of the examples used in the beginning of the course (gambling, Star Wars, Battle of the Sexes -- Ugh!), but towards the end they started to get a little better (Solar System, Movies -- Yay!). 

Overall I enjoyed learning R and I hope to learn more! 
If you have any questions or comments, feel free to post them below or [tweet at me](https://twitter.com/AndreaUrbanPhD){:target="_blank"}. 


<center> ![Certificate]({filename}/images/r_intro/r_certificate.png)
My Super Awesome Certificate! </center> 
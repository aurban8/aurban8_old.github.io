Title: The State of Jeopardy
Date: 2017-04-20 12:01
Category: Blog
Tags: jeopardy, chi-square, p-value, linear-regression, distribution-sampling, random-numbers
Slug: jeopardy-2-states-dollar
Authors: Andrea Urban
Summary: *California is the most popular state to appear as a Jeopardy answer. Popular U.S. states tend to have lower dollar values. After many assumptions, it is more lucrative to study popular U.S. states.*

*[California is the most popular state to appear as a Jeopardy answer.](#State-of-Jeopardy)  [Popular U.S. states tend to have lower dollar values.](#Money-Money-Money!) After many assumptions, it is more lucrative to study popular U.S. states.*


[Last time]({filename}./jeopardy_1_intro_clean.md), I cleaned the [Jeopardy data set](https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/) and created a JSON file to use for later. Well, later has arrived! Let's take a look at the dataset and look for some patterns.

{% notebook notebooks/jeopardy_2_states_values_years.ipynb cells[0:27] %}

<center> ![Donald Duck counting money, https://media.giphy.com/media/xTiTnqUxyWbsAXq7Ju/giphy.gif ]({filename}/images/donaldduck.gif)

[giphy](https://giphy.com/gifs/yosub-money-donald-duck-cash-xTiTnqUxyWbsAXq7Ju?utm_source=media-link&utm_medium=landing&utm_campaign=Media%20Links&utm_term=)  </center>

{% notebook notebooks/jeopardy_2_states_values_years.ipynb cells[27:47] %}

<center> ![Visual explanation of completing the squares, https://media.giphy.com/media/6wlrY2ABvHxDi/giphy.gif]({filename}/images/completesquare.gif)

[giphy](https://giphy.com/gifs/animation-math-geometry-6wlrY2ABvHxDi?utm_source=media-link&utm_medium=landing&utm_campaign=Media%20Links&utm_term=)
</center>

{% notebook notebooks/jeopardy_2_states_values_years.ipynb cells[47:] %}




The [jupyter notebook for this blog post can be found on github](https://github.com/aurban8/aurban8.github.io/blob/dev/content/notebooks/jeopardy_2_states_values_years.ipynb). [Next time]({filename}./jeopardy_3_states_wikipedia.md) I'll look into other datasets which might give more insight on why certain states are more likely to appear compared to others.
---
title: 'One should always play fairly when one has the winning cards: electoral viability and Twitter sentiment'
author: Javier Sajuria
type: post
date: 2014-09-09T17:40:45+00:00
url: /one-should-always-play-fairly-when-one-has-the-winning-cards-electoral-viability-and-twitter-sentiment/
dsq_thread_id:
  - "3002713005"
categories:
  - Uncategorized
tags:
  - Elections
  - Twitter

---
With [Jorge Fábrega][1], we we are currently working in a really interesting project to understand how public opinion surveys can be related to social media discussions. In a nutshell, we are interested in comparing public opinion data to what we can observe from Twitter. As a first step, we have prepared a draft chapter for an edited volume on digital methods for the social sciences, currently under review. The paper is still in a very early draft version, but I just wanted to share some of the early results.

The argument goes as follows. There is a <a href="https://www.google.co.uk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CCEQFjAA&url=http%3A%2F%2Farxiv.org%2Fabs%2F1204.6441&ei=djkPVNTgOsKVav2cgMgN&usg=AFQjCNH2dTMSbsk6aNcdafaOdSjjpVNpAQ&sig2=YGzGHx8ORzAtclFetfjZEg&bvm=bv.74649129,d.ZWU" target="_blank">great deal</a> <a href="http://www.tandfonline.com/doi/abs/10.1080/17512786.2012.663610" target="_blank">of research</a> <a href="http://ssc.sagepub.com/content/early/2010/09/24/0894439310386557.abstract" target="_blank">trying </a>to use social media data (mainly Twitter) to forecast elections, and some research on how to compare Twitter to candidate&#8217;s support on opinion polls. In the case of the former, most attempts have failed, while on the latter,  <a href="https://www.google.co.uk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0CDwQFjAD&url=http%3A%2F%2Fwww.kenbenoit.net%2Fpdfs%2FNDATAD2013%2FBeauchamp_twitterpolls_2.pdf&ei=TzkPVLLEHdDXaq-OgegB&usg=AFQjCNFZ3whmeTwt47rRKxrHdVEsiGvYsg&sig2=gLJ9RfX6NithL7FDFiAlEA" target="_blank">Nick Beauchamp</a> has managed to produce some interesting results. Our approach is slightly different: instead of looking at candidate support, we focus on support for certain policies. And instead of trying to predict support, we take one step back and think on other ways to relate both elements.

What came to our minds as a useful starting approach was to look at the sentiment on Twitter and how it relates to candidate support. We had two initial hypotheses:

  1. Supporters of candidates with higher electoral viability tend to tweet with a more positive tone overall.
  2. There is a correspondence between support for a policy and the tone used to tweet.

We used Chile as our case, and had two data sources: The CEP survey from October 2013, and Twitter data we collected previous to Chile&#8217;s presidential election last year.

Chile&#8217;s last election was quite competitive in terms of the number of candidates, but not in the vote share. President Bachelet had to go to a run-off election (something expectable with 9 candidates) against Evelyn Matthei, but she managed to get 62% of the votes on that round. A record share in the country&#8217;s recent history. In terms of electoral viability, 78% of the respondents of the CEP survey (2 months before the election) believed that Bachelet would win the presidency, with only 5% of people thinking that Matthei could get the job.

With that in mind, we processed our Twitter data to estimate two things: the political position of Twitter users in Chile, and the tone in which they tweet about 5 controversial topics:

  1. the possibility of constitutional reform through an assembly;
  2. a change in the current electoral system;
  3. the approval of an equal marriage law;
  4. abortion; and
  5. the ownership of the copper mines (they used to belong to the State).

To estimate the political position, we used retweet networks. In simple words, we setup an initial group of Twitter users with known preference for a candidates, and then performed some social network analysis of those who retweeted them. From there, we could move on to assign a probability for each user to support one of the candidates. We focused only on the four main candidates (Bachelet, Matthei, Enríquez-Ominami and Parisi), since they were the ones that generated more attention during the campaign.

To estimate the tone, we translated the lexicon from Wilson et al. and crafted our <a href="https://github.com/jsajuria/sentimiento" target="_blank">own version</a> of the <a href="https://github.com/timjurka/sentiment" target="_blank">sentiment R package</a> (used for sentiment analysis, of course). Each tweet was deconstructed into single words, which were then compared to the lexicon. Each word in the lexicon had assigned a polarity (positive or negative), and whenever there was a match between the words from the tweets and the lexicon, we assigned that polarity to the word. Then, the package uses the voter algorithm to determine that, given the number of matches, that tweet was itself positive or negative.

We first calculated the effect of candidate support on support for the policies mentioned above. our results (shown in the figure below) show that most respondents who supported one of the four candidates, in comparison to those who supported another or none, also support the policies. This was statistically significant for all the cases with a * in the figure.

[<img loading="lazy" class="aligncenter size-full wp-image-197" src="https://sajuria.com/wp-content/uploads/2014/09/Screen-Shot-2014-09-09-at-17.19.13.png" alt="Table_twt_cep" width="755" height="409" srcset="https://sajuria.com/wp-content/uploads/2014/09/Screen-Shot-2014-09-09-at-17.19.13.png 755w, https://sajuria.com/wp-content/uploads/2014/09/Screen-Shot-2014-09-09-at-17.19.13-300x162.png 300w, https://sajuria.com/wp-content/uploads/2014/09/Screen-Shot-2014-09-09-at-17.19.13-624x338.png 624w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 984px) 61vw, (max-width: 1362px) 45vw, 600px" />][2]

&nbsp;

In the case of Twitter, since our sampling was not probabilistic, we were more concerned about the direction of the relationship rather than the significance. Our dependent variable was the likelihood of a tweet having a positive tone. The results can be seen in the figure, and the most surprising feature is the decrease in probability for a positive tone when talking about equal marriage.

As we expected, supporters of Bachelet had a higher tendency to tweet with a positive tone, overall. Also, whenever there is a statistically significant relationship between supporting Bachelet and supporting a policy (e.g. electoral reform, abortion or copper mines ownership) that had a correlate with an increase in the probability of a positive tone on Twitter.

However, our second hypothesis suffered from a different fate. As you can observe, there is some decoupling between the support for a policy and the likelihood of a positive tone. Let&#8217;s look at the case of supporters of Enríquez-Ominami. aAlthough they seem keen to support all of the reforms, the tone they use when they tweet is not positive in most cases. We see a similar behaviour in some of the supporters for other candidates as well

We are still in the stage of making sense of these results, and thinking about possible expansions of this research. In the meantime, this is a nice starting point, and provides some insightful information on how to use Twitter data, not to replace, but to complement classical public opinion research.

 [1]: http://www.twitter.com/jorgefabrega
 [2]: https://sajuria.com/wp-content/uploads/2014/09/Screen-Shot-2014-09-09-at-17.19.13.png
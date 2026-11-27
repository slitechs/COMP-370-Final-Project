COMP 370 movie-post annotation: quality and agreement

Scope and files

The supplied October 16–17, 2026 UTC collection contains 742 distinct Bluesky posts. The three returned human-coder sheets each contain the same 347 post IDs, rather than complementary assignments. Sophia labeled 333 of those rows, Alexander 332, and Jerome 336. An AI assistant supplied provisional topic labels for the other 395 posts. The user reports that the professor allowed AI coding; this approval was not independently verified here.

After reviewing 80 posts flagged for possible eligibility problems, 14 were removed and 728 retained. The current files are eligibility_reviewed_annotations.xlsx (included posts, removed posts, and all 80 flag decisions), reviewed_included_posts.csv (analysis table), and removed_posts_log.csv (full removed text and reason). The full earlier merged_current_annotations.csv records human votes, decision type, and source; retain it as the provenance audit. The streamlined reviewed workbook supplied for the eligibility pass did not carry all those provenance columns.

One post receives exactly one of six topics: REACT (overall appraisal/feeling), CONTENT (story, people, meaning), CRAFT (filmmaking/performance), VIEWING (plans/access/theater experience), CIRC (marketing, coverage, commercial discussion), or HUMOR (joke/parody as the main point). Film identity and sentiment are separate from the topic. Eligibility is separate from both.

Agreement before reconciliation

Agreement is measured only on the original human labels, before majority voting, assistant adjudication, or eligibility removal. Blank votes are excluded pairwise. There are 319 posts with three nonblank human labels: 175 unanimous (54.9%), 126 with a 2–1 split (39.5%), and 18 with three different labels (5.6%). Thus 301/319 (94.4%) have at least two matching votes, which should not be confused with unanimity.

Coders

Posts both labeled

Exact matches

Raw agreement

Cohen's κ

Sophia–Alexander

323

225

69.7%

0.6037

Sophia–Jerome

325

199

61.2%

0.4895

Alexander–Jerome

328

240

73.2%

0.6227

On the 319 complete three-coder rows, the average pairwise agreement is 68.0% and Fleiss' κ = 0.5695, computed from the six-category vote counts per post. These are descriptive reliability statistics, not scores for the 728-row final dataset. Cohen's κ values use different complete-case sets because of blank cells. Agreement was planned on 150 shared posts but, because the returned files all contained the same 347 IDs, the observed overlap is 347. Do not present the 395 AI-only rows as three-coder agreement data.

The 347 shared posts also include 13 with two agreeing votes and one blank, six with two conflicting votes and one blank, six with only one vote, and three with no human vote. Several blanks contain explicit eligibility notes; they were not interpreted as a seventh topic. Before exclusion the merged working file used 175 unanimous labels, 126 2–1 majority labels, 13 two-agree/one-blank labels, six single-human-vote labels, 24 assistant choices without a majority, three assistant choices without any human votes, and 395 AI-only labels. These categories sum to 742. Following eligibility review, 341 shared human-coded rows and 387 AI-only rows remain among the 728 included posts.

What the disagreement shows

REACT versus CONTENT/CRAFT. Sophia–Jerome disagreed 29 times on REACT/CONTENT and 25 on REACT/CRAFT; Sophia used CRAFT 39 times across her 347 assigned posts, versus Jerome's 8. Coders differed in whether a specific observation about story, filmmaking, or performance outweighed a brief general verdict.

REACT versus VIEWING. Alexander–Jerome disagreed 18 times on this pair. “Go see it” can function as a recommendation, while a ticket, showtime, or actual screening experience belongs to VIEWING.

CIRC versus a substantive point. A review link or trailer mention alone tends to be CIRC; a post that itself interprets a character, theme, or technique belongs to CONTENT or CRAFT. Counting linked material that coders did not read would change the task.

HUMOR versus another topic. Wordplay and invented scenarios are HUMOR when the joke is the post's main point; “lol” or a witty recommendation does not override a substantive topic.

The κ values show meaningful but imperfect agreement. Majority coding resolves a label for analysis; it does not increase the measured inter-coder reliability. Assistant adjudication is a documented judgment, not a human consensus.

Eligibility decisions and removed posts

Only the 80 previously flagged rows were individually reviewed in this pass. Fourteen were excluded; the other 66 were kept. All 662 previously unflagged rows remain in the dataset without a new post-by-post eligibility audit. Reasons and full text appear in the Removed posts and Flag review tabs of the reviewed workbook.

Post ID

Reason for exclusion

45befb6454f9c69b

Portuguese headline and surrounding text.

f56b4027da9efbf1

Substantially Portuguese post.

efa5c0dca463f405

Substantially Portuguese post.

24b3f90e91b26e47

Explicitly about the Ang Lee/Emma Thompson 1995 adaptation.

a2352c356645cc04

Selected film is a parenthetical aside; another film is evaluated.

3617a2fb94d4d492

Discusses an unrelated post under a search trend rather than the film.

8603565e58a5b98c

Uses Whalefall as a hashtag while asking about ocean movies generally.

8931e2bec4fa3400

Meaning depends on an unseen image; text has no discernible film topic.

1ef53df975f6d358

Reviews The Devils; selected title only identifies other audience members.

6a04a739bb4168d5

Title correction with no discernible film or viewing point.

4accfc20e291c785

Selected film is an incidental release mention among unrelated films.

6d90b223b176da20

Bare film title and “apparently?” give insufficient context.

bdd43e72ee48a004

Film hashtags plus an opaque link, with no readable topic in the post.

a2519ba51ac65b3f

Generic follow-me request and opaque link; hashtag does not establish a film-related point.

The retained dataset has 527 posts mentioning You Can See Everything, 165 mentioning Whalefall, and 44 mentioning Sense and Sensibility. These mention counts overlap when a post names more than one film; they should not be added to obtain 728. The original collection had 535, 170, and 45 mentions respectively. The focal-film topic percentages should use 527 as the denominator under these decisions. The six topic counts across all 728 retained posts are REACT 262, VIEWING 178, CIRC 111, CONTENT 83, CRAFT 48, and HUMOR 46; these are not the focal-film percentages.

Six retained flagged rows had an obvious topic correction during eligibility review: 52dd3fca703dec5e HUMOR→VIEWING, ca3efae8b39f7906 CIRC→VIEWING, 3e98284ebad057b1 CIRC→VIEWING, dcbf2cef914ee311 REACT→VIEWING, 7e6afc7f6717f506 REACT→CIRC, and b04b9300091ea779 VIEWING→CIRC. Their reasons are in the Flag review tab. These are assistant review decisions, not votes by the three coders.

Recommended clarification to the taxonomy

Keep the six topics. Add these explicit rules to a versioned future guide, with one real post example for each:

Specificity: If the text develops a claim about plot, depicted people, meaning, acting, editing, or visual form, use CONTENT or CRAFT even when it begins or ends with “great film.” A bare score or emotional reaction is REACT.

Viewing versus recommendation: A plan, ticket, showtime, availability, film log, or account of the audience is VIEWING. “You should see it” plus praise, without a concrete viewing event or access issue, is REACT.

Coverage versus interpretation: A bare review link, review announcement, aggregate score, box-office result, or trailer promotion is CIRC. Classify the post's own substantive claim instead when it develops one; never follow the link to decide.

Humor: Reserve HUMOR for a joke or parody that is the main message. Do not infer a joke from informal language alone.

Eligibility before topic: A name-only post can be a viewing log or a release announcement if its own text supplies that context. Exclude an opaque link/hashtag, non-English text, an older adaptation, or a passing mention where the post's topic cannot be assigned from its text. Record exclusions independently of topic labels.

Do not silently apply a revised guide retroactively to claim higher agreement. If the group adopts new definitions for the submitted analysis, document the version and have the affected posts recoded or adjudicated consistently. The existing guide's general rules already point in these directions; the extra examples and precedence language are intended to reduce the observed ambiguity.

Reproducibility and reporting limits

The 728-row included file is usable for descriptive topic counts and TF-IDF after the group accepts the documented eligibility and adjudication decisions. For the first research question, filter to eligible posts mentioning You Can See Everything and calculate each topic's percentage of 527, using the post topic once per post. For the coverage-volume question, use the eligible mention counts above and explain that multi-film posts count in each mentioned film's total. The group should report the original collection rules and search completeness separately; annotation cannot establish that the collection was unbiased. State clearly that the remaining 395 labels and 27 original no-majority/no-vote resolutions were made with AI assistance, as reported in the provenance file. An LLM category summary is a separate project requirement: record the model, exact prompt, and the labeled input used when that analysis is run.

# Movie post topic taxonomy guide

## Motivation

The project asks what percentage of English-language Bluesky posts mentioning *You Can See Everything* on October 16–17, 2026 discuss each topic. This taxonomy groups posts by **what the writer focuses on**. I first open-coded the 200 posts drawn from *You Can See Everything*, *Whalefall*, *Sense and Sensibility*, and posts mentioning multiple films. Initial descriptions were consolidated into six categories (these can be revised after annotation phase). The same guide applies to all three films. Film identity, positive or negative opinion, and number of likes are **not** topic codes.

**Unit and evidence.** One Bluesky post receives one main topic. Use only its written text; do not open links or infer what an attached image shows. Read the whole post before coding. The examples below are identified by post ID from the 200-post open-coding sample so the team can check each decision. 
## Topics

### REACT  Overall appraisal or felt response

**Definition:** The post mainly says whether the film is good or worth seeing, recommends it, expresses anticipation, or describes how watching it felt, without developing a more specific aspect.

**Include:** `59fbd5c8658d4042` calls *You Can See Everything* the best documentary the writer has seen. `7b54c93fd288d0d6` calls *Whalefall* fantastic and emotionally devastating.

**Exclude:** `9cd3997b8fc151b2` explains that the father and family story makes *Whalefall* resonate; code **CONTENT**, even though the writer liked it. `ed279a6d2daa2523` is about a missing local screening; code **VIEWING**.

**Edge case:** “Go see it” with general praise is REACT. An explicit observation about story, performance, or marketing takes precedence over a short “great movie” or star rating. A bare title with no discernible point is flagged for eligibility or insufficient context; do not invent an opinion.

### CONTENT  Story, people and meaning

**Definition:** The post discusses what happens in the film, its depicted people or relationships, themes, interpretation, ethics, or how the new film adapts its source story.

**Include:** `21ca6ba0169f3560` considers what the film’s title implies about Elizabeth Holmes. `9cd3997b8fc151b2` focuses on the family trauma in *Whalefall*. `2435e8a3407c0f16` discusses the sisters’ relationship in the new *Sense and Sensibility*.

**Exclude:** `a1bab3d5fe9c4423` focuses on photography, color, score and sets; code **CRAFT**. `3879933dbb99920d` reports Rotten Tomatoes scores without a substantive interpretation; code **CIRC**.

**Edge case:** A scene described for its plot revelation is CONTENT; a scene described for its editing or camera work is CRAFT. A review headline can be CONTENT if the headline itself makes a specific claim, as in `2e4c0b764413bd06` on Holmes and truth. Do not read the linked review.

### CRAFT  Filmmaking and performances

**Definition:** The post’s main point concerns direction, acting, editing, photography, sound, production design, structure, or pacing.

**Include:** `a1bab3d5fe9c4423` discusses 35 mm images, framing, score and sets. `b6b6fb1777e40474` argues the three-hour runtime is justified. `bc7ae7e41d8ba81a` describes how the film uses expectations of Nathan Fielder as a formal device.

**Exclude:** `21ca6ba0169f3560` interprets the title and Holmes’s portrayal; code **CONTENT**. `59fbd5c8658d4042` supplies only an overall verdict; code **REACT**.

**Edge case:** “The acting was great” is CRAFT if acting is the point; if it is an aside within a sustained overall reaction, choose REACT. `22d451b8feac0b50` says only “too dark”: this could mean visual lighting or tone. Mark the ambiguity rather than assuming which one.

### VIEWING  Plans, access and theater experience

**Definition:** The post mainly concerns plans to watch, ticket cost, availability, showtimes, what happened at a screening, or a shared audience experience.

**Include:** `ed279a6d2daa2523` complains that the film is not playing in Maine. `d4ff979e2b062f07` describes a sold-out screening and discussion afterward. `90c39eeb8d1ab19b` weighs the cost of a *Whalefall* ticket.

**Exclude:** `a67a642fe7167b8a` compares preview grosses and theater counts as a commercial result; code **CIRC**. `f9acbe6cbec2de83` recommends a film rather than describing a viewing plan; code **REACT**.

**Edge case:** “I saw it” before a detailed review is background, not the topic. A post listing films the writer plans to see is VIEWING. A post about sold-out shows as evidence of an industry trend is CIRC if that broader claim is its main point.

### CIRC  Marketing, coverage and commercial discussion

**Definition:** The post focuses on trailers, advertising, release strategy, professional reviews as news or promotion, critic aggregates, box office, awards, or broader film-industry discussion.

**Include:** `a86ef2997585815d` discusses *Whalefall*’s advertising tagline. `a67a642fe7167b8a` reports an A24 preview record. `3f6cc6f6c294c289` criticizes a trailer for omitting a cast member.

**Exclude:** `2e4c0b764413bd06` states a particular interpretation of Holmes in its headline; code **CONTENT**. `ed279a6d2daa2523` asks about an actual local showing; code **VIEWING**.

**Edge case:** A post that only announces or links a review belongs here. If its own text develops a point about acting, story, or quality, code that point instead. Use CIRC for criticism of remakes as an industry practice; use CONTENT for a specific comparison of how an adaptation tells its story.

### HUMOR  Joke or parody as the main point

**Definition:** The post is primarily a film-related joke, wordplay, skit, or absurd imagined scenario, with no more developed substantive point.

**Include:** `43c4682b1a11ee02` is a dialogue sketch built around the title *You Can See Everything*. `71dc0c25a9b0f331` adds “for Tax Purposes” to the film’s title. `12a82c90607df295` invents an animal-mouth film franchise.

**Exclude:** `a86ef2997585815d` quotes a funny tagline to discuss an actual marketing choice; code **CIRC**. `7b54c93fd288d0d6` uses informal language but mainly reports an emotional reaction; code **REACT**.

**Edge case:** “lol,” sarcasm, or a funny adjective does not automatically make a post HUMOR. If the joke also makes a clear claim about a real screening, story, or trailer, code that claim. A post whose meaning depends entirely on an image unseen by coders should be flagged as insufficient context.

## Rules for mixed and questionable posts

1. Find the post’s **main developed point**. A concrete point about story or craft takes precedence over brief praise, a rating, “I saw it,” and a link. If two points remain equally developed, use the first one and record the alternative in the note column. Coders should not use the movie’s identity to break a tie.
2. If a post names several films, give the **post** one topic based on its main point. Film-match flags are tracked separately for the coverage question. A list of planned viewings is VIEWING; box-office comparisons are CIRC; comparison of themes is CONTENT.

### Flagged example
- `24b3f90e91b26e47` appears to praise the Ang Lee and Emma Thompson *Sense and Sensibility*, not the 2026 film; 
- `efa5c0dca463f405` is substantially Portuguese.




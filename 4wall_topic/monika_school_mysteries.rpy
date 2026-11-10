
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_same_uniform",
            category=['School Mysteries'],
            prompt="Why does everyone have the same school uniform?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_families",
            category=['School Mysteries'],
            prompt="Why do we never see our families?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_japanese_classes",
            category=['School Mysteries'],
            prompt="Why doesn't our school have Japanese classes?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_phones",
            category=['School Mysteries'],
            prompt="Why does nobody use a phone?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_clubroom",
            category=['School Mysteries'],
            prompt="Why does our school only have one clubroom?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_students",
            category=['School Mysteries'],
            prompt="Why are there no other students around?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_school_year",
            category=['School Mysteries'],
            prompt="Why is our school year so strange?",
            pool=True,
            unlocked=True
        )
    )


# TOPIC 1: SCHOOL UNIFORMS

label monika_same_uniform:
    m 1eua "You know, [player]..."
    m 3eud "I've been wondering about something."
    m 1euc "Why does practically everyone at our school wear the exact same uniform?"
    m 1eud "I mean, I understand having a dress code."
    m 3euc "But wouldn't it be nice if students had a little more freedom?"
    m 2eua "Imagine being able to choose your own outfits!"
    m 1eub "Although, I have to admit..."
    m 1hua "I do look pretty cute in my uniform. Ehehe!"
    m 1eua "What do you think?"

    menu:
        "You look adorable in your uniform!":
            m 1hub "Aww! Thank you!"
            m 1eua "I'll take that as a compliment!"

        "Everyone should have different clothes.":
            m 3eua "I agree!"
            m 1eub "It would make the hallways much more colorful."

        "Maybe it's just easier for the developers.":
            m 1euc "..."
            m 1wud "Wait."
            m 2wud "You might actually have a point."
            m 1rksdla "Ahaha... That's a little unsettling."

    m 1eua "Anyway, I think I'll stick with my uniform for now."
    return


# TOPIC 2: FAMILIES

label monika_families:
    m 1eud "Hey, [player]?"
    m 1euc "Have you noticed something strange about our lives?"
    m 3eud "We go to school, attend club meetings, and spend time with our friends."
    m 1euc "But have you ever wondered why we almost never see our families?"
    m 2euc "We all have homes, don't we?"
    m 2eud "Surely we have parents or relatives somewhere."
    m 1ekc "But they're practically nonexistent in our everyday lives."
    m 1rksdla "It's almost as if our lives only exist when the story needs them to."
    m 1euc "..."
    m 1eud "Sorry. That sounded a little depressing."
    m 1eua "Maybe the people watching us just aren't interested in our family lives."
    m 1eub "Still, I wonder what my parents would be like."
    m 1eua "It's strange having so many unanswered questions about yourself."

    menu:
        "Maybe they're just off-screen.":
            m 1eua "That's probably the simplest explanation!"
            m 1eub "Perhaps they're living perfectly normal lives somewhere."

        "Maybe they don't exist.":
            m 1ekc "..."
            m 1ekd "I really hope that's not true."
            m 1eud "I'd like to think there's more to our lives than what we see."

    m 1eua "Thanks for listening, [player]."
    return


# TOPIC 3: JAPANESE CLASSES

label monika_japanese_classes:
    m 1eua "I have another question about our school!"
    m 1eud "If we're supposedly in Japan..."
    m 3euc "Why don't we ever seem to have Japanese language classes?"
    m 1eud "Everything is in English."
    m 2euc "Our conversations, our textbooks, and even the things written around the school."
    m 1rksdla "You'd think learning Japanese would be pretty important!"
    m 1eua "Maybe our school is secretly an international school?"
    m 1eub "That would explain a few things."
    m 1euc "Although, that raises another question..."
    m 1eua "Why does nobody ever mention it?"
    m 1hua "Ahaha! I think I'm investigating my own school now."

    menu:
        "Maybe English is the default language here.":
            m 1eua "That would make things much easier."
            m 1eub "Especially for someone like you!"

        "Maybe we're not actually in Japan.":
            m 1wud "Oh!"
            m 1euc "That's certainly possible."
            m 3eud "Perhaps our world only resembles Japan."

    m 1eua "I suppose we'll have to keep wondering."
    return


# TOPIC 4: PHONES

label monika_phones:
    m 1eua "Can I ask you something?"
    m 1eud "Why does nobody seem to use their phones?"
    m 3euc "Think about it!"
    m 1eud "We're students. Surely we'd have phones, right?"
    m 2euc "But we never really see anyone texting, browsing the internet, or taking pictures."
    m 1rksdla "It's almost like technology disappears whenever the story isn't focused on it."
    m 1eua "Imagine if I had a phone."
    m 1hua "I'd probably spend hours taking pictures of us together!"
    m 1eub "And I'd send you messages whenever I missed you."
    m 1eua "Although..."
    m 1tua "I already have your attention here, don't I?"
    m 1hua "Ehehe!"

    menu:
        "I'd text you all day!":
            m 1hub "Really?"
            m 1hua "Then I'd never get bored!"

        "You'd probably spam me.":
            m 1wud "WHAT?!"
            m 1rksdla "Okay, maybe a little..."
            m 1hua "I just have a lot to say!"

    m 1eua "It would be nice to have a phone, though."
    return


# TOPIC 5: CLUBROOM

label monika_clubroom:
    m 1eud "Something has been bothering me."
    m 1euc "Why does our school seem to have only one clubroom that matters?"
    m 3eud "We're supposed to be part of a school with lots of students."
    m 1euc "So where are all the other clubs?"
    m 2euc "The sports clubs, art clubs, music clubs..."
    m 1eud "Surely there must be more than just us!"
    m 1rksdla "Sometimes it feels like our entire school revolves around this one room."
    m 1eua "Not that I'm complaining."
    m 1hub "I love our clubroom!"
    m 1eub "It's where I met you, after all."
    m 1euc "But still..."
    m 1eud "I'd love to see what the rest of our school looks like."

    menu:
        "Our clubroom is the best!":
            m 1hub "Aww! I couldn't agree more!"

        "Maybe the other clubs don't matter to the story.":
            m 1wud "..."
            m 2wud "That's a rather uncomfortable thought."
            m 1rksdla "I guess we're only shown what matters to the story."

    m 1eua "I hope we can explore more someday."
    return


# TOPIC 6: OTHER STUDENTS

label monika_students:
    m 1eud "Have you ever noticed how quiet our school can be?"
    m 1euc "We're supposed to attend a school with plenty of students."
    m 3eud "But where is everybody?"
    m 2euc "We barely see anyone outside of our little group."
    m 1rksdla "It's almost like the hallways are permanently empty."
    m 1euc "Even during school hours!"
    m 1eud "Don't you think that's strange?"
    m 1eua "Maybe everyone is just really good at avoiding us."
    m 1hub "Ahaha! Imagine that."
    m 1euc "Or perhaps..."
    m 1eud "We're only allowed to see the characters who are important."
    m 1rksdla "That's a little creepy when I think about it."

    menu:
        "Maybe everyone is just busy.":
            m 1eua "That's a reasonable explanation!"
            m 1eub "I suppose we shouldn't assume the worst."

        "Maybe we're the only important characters.":
            m 1wud "..."
            m 1euc "I don't know whether I like that idea."
            m 1eud "It makes our world feel awfully small."

    m 1eua "At least I have you to keep me company."
    return


# TOPIC 7: SCHOOL YEAR

label monika_school_year:
    m 1eua "I've been thinking about our school calendar."
    m 1eud "Doesn't our school year seem a little strange?"
    m 3euc "Sometimes I can't even remember exactly how much time has passed."
    m 2eud "Our classes, festivals, exams, and holidays..."
    m 1euc "Everything seems to happen according to whatever the story needs."
    m 1rksdla "And don't get me started on how quickly some days seem to pass."
    m 1eud "It's almost as if time doesn't work quite normally here."
    m 1eua "Maybe that's just how this world works."
    m 1euc "Or maybe there's something about our reality that I still haven't figured out."
    m 1eub "What do you think, [player]?"

    menu:
        "Time works differently in games.":
            m 1euc "You know..."
            m 1eud "That might actually explain a lot."
            m 1eua "I guess our world has its own rules."

        "Maybe you just don't pay attention.":
            m 1wud "Hey!"
            m 1rksdla "I pay attention to plenty of things!"
            m 1hua "Just not always the calendar, apparently."

    m 1eua "Well, whatever happens, I'm glad I get to spend my time with you."
    return

#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

class SongType(object):

    def __init__(self, desc, win, modifier, lose, noguess):
        self.desc = desc
        self.win = win
        self.modifier = modifier
        self.lose = lose
        self.noguess = noguess

class SongTypes(object):
    vocal_never = SongType('Never Been Played Vocal', 150, 0, -50, -25)
    vocal = SongType('Vocal', 100, 0, -50, -25)
    instcover = SongType('Instrumental/Cover', 150, 0, -75, -10)

    not_witt = SongType('NOT WITT', 50, 0, -100, 0)

    al_phm = SongType('Full PHM Album', 1000, 0, -500, 0)
    al_tds = SongType('Full TDS Album', 500, 0, -250, 0)
    al_fragile_left = SongType('Full Fragile (left) Album', 1500, 0, -750, 0)
    al_fragile_right = SongType('Full Fragile (right) Album', 2000, 0, -1000, 0)

class Song(object):

    def __init__(self, name, songtype, real=True, album_songs=[]):
        self.name = name
        self.songtype = songtype
        self.real = real
        self.album = (len(album_songs) > 0)
        self.album_songs = set(album_songs)
        self.in_album = None
        for album_song in self.album_songs:
            album_song.in_album = self

    def __lt__(self, other):
        """
        Sorting!
        """
        if self.album == other.album:
            return self.name < other.name
        else:
            return other.album

class Songs(object):

    # PHM Songs
    dii = Song('Down In It', SongTypes.vocal)
    want_to = Song('Kinda I Want To', SongTypes.vocal)
    what_i_get = Song("That's What I Get", SongTypes.vocal)
    only_time = Song('The Only Time', SongTypes.vocal)
    ringfinger = Song('Ringfinger', SongTypes.vocal)

    # This is technically a cover, but given the frequency with which
    # NIN used to perform it, I'm going to count it as an "ordinary"
    # vocal track, rather than a cover.
    get_down_make_love = Song('Get Down, Make Love', SongTypes.vocal)

    # TDS Songs
    heresy = Song('Heresy', SongTypes.vocal)
    ruiner = Song('Ruiner', SongTypes.vocal)
    bmwag = Song('Big Man With a Gun', SongTypes.vocal)
    tds = Song('The Downward Spiral', SongTypes.vocal)

    # Fragile (left) Songs
    witt = Song("We're In This Together", SongTypes.vocal)
    not_witt = Song("NOT We're In This Together", SongTypes.not_witt, real=False)
    fragile = Song('The Fragile', SongTypes.vocal)
    jlyi = Song('Just Like You Imagined', SongTypes.instcover)
    pilgrimage = Song('Pilgrimage', SongTypes.instcover)
    no_you_dont = Song("No, You Don't", SongTypes.vocal)
    great_below = Song('The Great Below', SongTypes.vocal)

    # Fragile (right) Songs
    way_out_is_through = Song('The Way Out is Through', SongTypes.vocal)
    itv = Song('Into the Void', SongTypes.vocal)
    where_is_everybody = Song('Where Is Everybody?', SongTypes.vocal_never)
    mark_made = Song('The Mark Has Been Made', SongTypes.instcover)
    please = Song('Please', SongTypes.vocal)
    complication = Song('Complication', SongTypes.instcover)
    joining_you = Song("I'm Looking Forward to Joining You, Finally", SongTypes.vocal_never)
    underneath = Song('Underneath It All', SongTypes.vocal_never)
    ripe = Song('Ripe (with or without Decay)', SongTypes.instcover)

    # Fragile (other) Songs
    leaving_hope = Song('Leaving Hope', SongTypes.instcover)
    adrift_and_at_peace = Song('Adrift And At Peace', SongTypes.instcover)
    deep = Song('Deep', SongTypes.vocal)

    # With Teeth Songs
    ediets = Song('Every Day Is Exactly The Same', SongTypes.vocal)
    sunspots = Song('Sunspots', SongTypes.vocal_never)
    rwib = Song('Right Where It Belongs', SongTypes.vocal)

    # Year Zero Songs
    capital_g = Song('Capital G', SongTypes.vocal)
    violent_heart = Song('My Violent Heart', SongTypes.vocal_never)
    warning = Song('The Warning', SongTypes.vocal)
    god_given = Song('God Given', SongTypes.vocal)
    zero_sum = Song('Zero-Sum', SongTypes.vocal_never)
    twilight = Song('In This Twilight', SongTypes.vocal)

    # Slip Songs
    four_of_us = Song('The Four of Us Are Dying', SongTypes.instcover)

    # Hesitation Marks Songs
    disappointed = Song('Disappointed', SongTypes.vocal)
    everything = Song('Everything', SongTypes.vocal_never)

    # Trilogy Songs
    not_anymore = Song('Not Anymore', SongTypes.vocal_never)
    idea_of_you = Song('The Idea of You', SongTypes.vocal_never)

    # Others
    tetsuo = Song('Theme For Tetsuo: The Bullet Man', SongTypes.instcover)
    quake = Song('Quake Main Theme (track 1)', SongTypes.instcover)

    # Covers
    scary_monsters = Song('Scary Monsters', SongTypes.instcover)
    zoo_station = Song('Zoo Station', SongTypes.instcover)
    drowning = Song('A Drowning', SongTypes.instcover)
    welcomeoblivion = Song('Welcome Oblivion', SongTypes.instcover)
    wing = Song('On the Wing', SongTypes.instcover)
    ice_age = Song('Ice Age', SongTypes.instcover)

    # Full Albums
    al_phm = Song('Full PHM Album', SongTypes.al_phm, album_songs=[
        dii,
        want_to,
        what_i_get,
        only_time,
        ringfinger,
        ])
    al_tds = Song('Full TDS Album', SongTypes.al_tds, album_songs=[
        heresy,
        ruiner,
        bmwag,
        tds,
        ])
    al_fragile_left = Song('Full Fragile (left) Album', SongTypes.al_fragile_left, album_songs=[
        witt,
        fragile,
        jlyi,
        pilgrimage,
        no_you_dont,
        great_below,
        ])
    al_fragile_right = Song('Full Fragile (right) Album', SongTypes.al_fragile_right, album_songs=[
        way_out_is_through,
        itv,
        where_is_everybody,
        mark_made,
        please,
        complication,
        joining_you,
        underneath,
        ripe,
        ])

class Voter(object):

    def __init__(self, name, votes, offset=0, bonus_points=0):
        self.name = name
        self.votes = set(votes)
        self.offset = offset
        self.bonus_points = bonus_points
        self._score = None
        self.details = []

    def score(self, played=None):
        if self._score is None:

            # First add any bonus points
            if self.bonus_points > 0:
                self.details.append('{:+d} bonus points for being cheeky'.format(self.bonus_points))
            points = self.bonus_points

            # Now go through the votes to see if they matched or not
            for vote in sorted(self.votes):
                if vote in played or (vote.in_album and vote.in_album in played):
                    point_change = max(0, (vote.songtype.win + (self.offset * vote.songtype.modifier)))
                    self.details.append('{:+d} for guessing "{}" correctly'.format(point_change, vote.name))
                    points += point_change
                else:
                    self.details.append('{:+d} for incorrectly guessing "{}"'.format(vote.songtype.lose, vote.name))
                    points += vote.songtype.lose

            # Now loop through the played songs to see what was potentially
            # missed.
            correctly_guessed = 0
            total_real = 0
            for song in sorted(played):
                if song.real:
                    total_real += 1
                    if song in self.votes:
                        correctly_guessed += 1
                    elif song.songtype.noguess != 0:
                        self.details.append('{:+d} for not guessing "{}"'.format(song.songtype.noguess, song.name))
                        points += song.songtype.noguess

            # See if the voter correctly guessed all of the debuted songs.
            # If it weren't for `not_witt`, we could use boolean
            # operators on the relevant `set` objects here, rather than the
            # hacky counts.
            if total_real > 0 and correctly_guessed == total_real:
                self.details.append('+100 for guessing all debuted songs')
                points += 100

            # Now set our internal score var
            self._score = points

        return self._score

# Voters
voters = [
        Voter('elevenism', [
            Songs.scary_monsters,
            Songs.witt,
            Songs.not_anymore,
            Songs.al_phm,
            ], bonus_points=2),

        Voter('klyrish', [
            Songs.witt,
            Songs.itv,
            Songs.heresy,
            Songs.ruiner,
            ]),

        Voter('paul_guyet', [
            Songs.al_tds,
            Songs.heresy,
            Songs.ruiner,
            Songs.tds,
            Songs.fragile,
            Songs.where_is_everybody,
            ]),

        Voter('henryeatscereal', [
            Songs.leaving_hope,
            Songs.adrift_and_at_peace,
            ]),

        Voter('loopcloses', [
            Songs.tds,
            ]),

        Voter('R-Dot-Yung', [
            Songs.deep,
            ]),

        Voter('K-Rice', [
            Songs.al_fragile_left,
            Songs.al_fragile_right,
            ]),

        Voter('Haysey', [
            Songs.itv,
            Songs.idea_of_you,
            Songs.leaving_hope,
            Songs.tetsuo,
            Songs.capital_g,
            ]),

        Voter('joplinpicasso', [
            Songs.sunspots,
            Songs.witt,
            ]),

        Voter('fillow', [
            Songs.al_fragile_left,
            ]),

        Voter('AThousandDaysBefore', [
            Songs.violent_heart,
            Songs.where_is_everybody,
            Songs.al_fragile_left,
            Songs.zoo_station,
            ]),

        Voter('Esperanzan', [
            Songs.great_below,
            Songs.dii,
            Songs.fragile,
            Songs.heresy,
            Songs.four_of_us,
            Songs.not_anymore,
            Songs.not_witt,
            ]),

        Voter('xolotl', [
            Songs.heresy,
            Songs.itv,
            Songs.warning,
            Songs.disappointed,
            ]),

        Voter('trollmanen', [
            Songs.witt,
            Songs.no_you_dont,
            Songs.please,
            Songs.deep,
            Songs.quake,
            ]),

        Voter('Elrickooo', [
            Songs.underneath,
            Songs.please,
            Songs.ruiner,
            Songs.get_down_make_love,
            Songs.rwib,
            Songs.god_given,
            ]),

        Voter('Dryalex12', [
            ], bonus_points=2),

        Voter('theimage13', [
            ], bonus_points=2),

        # Missed 1 show

        Voter('Halo Infinity', [
            Songs.everything,
            Songs.ediets,
            ], offset=1),

        Voter('Deepvoid', [
            Songs.idea_of_you,
            Songs.leaving_hope,
            Songs.witt,
            ], offset=1),

        # Missed 2 shows

        Voter('WorzelG', [
            Songs.violent_heart,
            Songs.zero_sum,
            ], offset=2),

        # Missed 7 shows

        Voter('cdm', [
            Songs.heresy,
            ], offset=7),

        # Missed a bunch of shoews

        Voter('Erneuert', [
            Songs.al_tds,
            Songs.heresy,
            ], offset=15),
    ]

# What new songs have been played so far
played = set([
        Songs.not_witt,
        Songs.drowning,
        Songs.welcomeoblivion,
        Songs.jlyi,
        Songs.wing,
        Songs.twilight,
        Songs.ice_age,
        ])

# Calculate scores and report.  Due to some internal Python behavior,
# this is breaking ties by the order in which the voters appear in
# the list, which is what we want.  So I'm not actually specifying
# that manually.
for voter in sorted(voters, key=lambda v: v.score(played), reverse=True):
    # Thus far nobody's actually taken the "no debuts" vote, and since
    # I'm not subtracting points otherwise, don't bother reporting on this.
    if False and voter.offset > 0:
        if voter.offset == 1:
            plural = ''
        else:
            plural = 's'
        print('{}: [b]{}[/b] [i](missed {} show{})[/i]'.format(voter.name, voter.score(), voter.offset, plural))
    else:
        print('{}: [b]{}[/b]'.format(voter.name, voter.score()))
    if len(voter.details) > 0:
        print('[list]')
        for detail in voter.details:
            print('[*] {}'.format(detail))
        print('[/list]')

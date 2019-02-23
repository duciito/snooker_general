# snooker_general

A CLI representation of the snooker.org API with a few more things.

(still at a very early stage of development)

#### some things that are troubling the continued development of the project
* most things you can get only by ID and the api provides no list of IDs to reference from
* i'll most probably have to scrape a few other snooker websites for some functions to be complete

#### TODO
* ~~add the option to go back after each action~~
* ~~group live matches by event~~
* group event matches by round
* auto-update of live matches (partially working)
* ~~move the display functions to a separate module~~
* limit showed season events to only bigger ones (will remove some irrelevant tournaments)
* try to make all requests async in the near future
* look into curses as it may help with cli stuff
* add the option to check all matches in an event

# DB Notes

Link: https://www.dropbox.com/s/n7mh7vs28x7v3hn/DB%20schemas.jpg?dl=0
User Data [user_id, username, first_name, last_name]
Event Data [event_id, user_id, venue_id, event_score] (note, each row will have different events and users for each event)
Venue List [venue_id, venue_name, address, lat, lng, type, event_id] (https://developers.google.com/maps/articles/phpsqlajax_v3)
## Description
This is a Python application that allows you to connect to your Arlo cameras in order to download every single video onto a local machine. This could be considered a workaround to Arlo's cloud subscription, where they allow you to keep your documented videos on their servers for 30 days (or whatever it is).

I'll be hosting all of my videos on a BeagleBone Black with a 64GB microSD card attached to it, so I can store *quite* a bit of footage without having to pay for a subscription to the service. 

### To-Do
#### Bug Fixes
- [x] Iterate over the *video_delete* variable, as I need to extract (from each item in the list) item[1], which is what I need to delete from the local filesystem
- [ ] If the host machine loses connection to Wi-Fi, the application will shut down due to non-response to the Arlo servers. Keep the application open and running until wifi has been reestablished, and use the same credentials to log back in

#### Features
- [ ] Include any other cameras that I might have

#### Other
- [ ] Refactor to make things look more **POOP-y** (Python Object-Oriented Programming... -y)
<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/DanTcheche/your_social_life_bot">
    <img src="media/your_social_life_bot.png" alt="Logo">
  </a>

  <h3 align="center">Your social life bot</h3>

  <p align="center">
    Telegram bot to help you with your social life.
    <br />
    <a href="https://github.com/DanTcheche/your_social_life_bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/DanTcheche/your_social_life_bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/DanTcheche/your_social_life_bot/issues">Request Feature</a>
    ·
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

With the exponential growth of Telegram in the last month I found myself
interested in building some useful bots to help in the daily life.

The current main functionalities are:
* Birthdays management.
  * Adding birthdays.
  * Listing birthdays.
  * Getting next birthday (WIP).
  * Notification when it's someone's birthday (WIP).
    
* Events management.
  * Adding events.
  * Listing next events.
  * Getting next event.
  * Attending or missing events.
  * Deleting events.  
  * Notification the day of an event (WIP).

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)
* [MongoDB](https://www.mongodb.com/)

<!-- GETTING STARTED -->
## Getting Started

Open [@BotFather](https://telegram.me/botfather) on Telegram and create a new bot with the `/newbot` command.

Assign it a name. This name won't be the one that is shown on each message, so you can name it whatever you want.

@BotFather will grant you a Token. This is the TOKEN you'll need to interact with the BOT. Keep it private!
In the `main.py` file replace "YOUR TOKEN with the given TOKEN".

![./media/bot_father.png](media/bot_father.png)

You can also use the `/setcommands` to define the uses your bot has on the '/' icon:

![./media/bot_father_add_commands.png](media/bot_father_add_commands.png)

### Installation

1. Make sure you are running python:
    1. Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) for installing pyenv
    1. See which python versions are available: `pyenv install --list`
    1. Install python 3. Example: `pyenv install 3.6.6` (3.6.6 or higher)
    1. `pyenv shell 3.6.6`

    
2. Install bot dependencies:

```sh
  pip install -r requirements.txt 
```

3. Run the app:
```sh
   python3 main.py
```



<!-- USAGE EXAMPLES -->

## Usage

Use `/help` to list all commands.
```sh
    Commands: 
    /help - A little help.
    /birthdays - List all birthdays.
    /add_birthday name(one word) dd/mm/yyyy - Add a birthday.
    /events - List all events.
    /add_event name(one word) dd/mm/yyyy hh:mm place - Add an event.
    /delete_event event_name- Deletes an event.
    /attend_event event_name - Adds you as a participant.
    /miss_event event_name - You are not assisting the event.
```

List all future events:
```text
    /events
```

Add event example:
```text
    /add_event RandomEvent 26/01/2021 16:00 Somewhere near
```

Attend event example:
```text
    /attend_event RandomEvent
```

Miss event example:
```text
    /miss_event RandomEvent
```

Delete event example:
```text
    /delete_event RandomEvent
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/DanTcheche/your_social_life_bot/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Dan Tcheche - dancheche@hotmail.com

Project Link: [https://github.com/DanTcheche/your_social_life_bot](https://github.com/DanTcheche/your_social_life_bot)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DanTcheche/your_social_life_bot.svg?style=for-the-badge
[contributors-url]: https://github.com/DanTcheche/your_social_life_bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DanTcheche/your_social_life_bot.svg?style=for-the-badge
[forks-url]: https://github.com/DanTcheche/your_social_life_botnetwork/members
[stars-shield]: https://img.shields.io/github/stars/DanTcheche/your_social_life_bot.svg?style=for-the-badge
[stars-url]: https://github.com/DanTcheche/your_social_life_bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/DanTcheche/your_social_life_bot.svg?style=for-the-badge
[issues-url]: https://github.com/DanTcheche/your_social_life_bot/issues

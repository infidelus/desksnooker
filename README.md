# Desk Snooker

A realistic snooker game for the Meta Quest 3 that runs straight from the browser using WebXR. A full-size table appears in your room in passthrough, or in a snooker club or a championship arena in full VR. It's designed so you can rest your bridge hand on a real desk while you cue, and the table can be moved and turned with the thumbsticks to suit your space. It also plays on a computer with a mouse and keyboard.

## Features

- **Physics:** stun, screw, side, swerve and massé; cushions with proper jaws; balls that drop into the pocket nets. The cue can't pass through balls or the cushion rail, so a ball tight on a cushion can only be struck high, as in the real game.
- **Rules:** full professional rules, including foul and a miss, free balls, touching ball, push strokes, re-spotted black and colour nomination, with a referee who calls the score.
- **Opponents:** 24 computer players, from pub regular to snooker legend. The weakest go for the easiest pot and miss plenty; the best pot reliably, play safe, escape snookers and think two shots ahead for position.
- **Championship:** an 8- or 16-player championship with an amateur or pro field (each match is your chosen best-of length, the final two frames longer), played in an arena with a crowd, applause and a live scoreboard, and a trophy for the winner.
- **Rests (optional):** shots you couldn't reach in real life are played on the rest, with an extension, the long rest, the spider or the swan as needed, held in your bridge hand. Guided mode makes them harder to play, as they are for real.
- **Online matches:** play someone on another computer or headset, with voice chat. One player hosts and gets a five-digit room code; the other joins with it. Players connect directly (WebRTC, via the free PeerJS service), so there's no server to run.
- **Coach:** seven lessons (cue-ball control, cut angles, doubles, one- and two-cushion escapes, swerve and the break-off), plus a tip for any position in practice.
- **Venues:** a snooker club with a bar and trophy cabinet, the championship arena, or your own room in passthrough.

## Playing

**Play it now: https://infidelus.github.io/desksnooker/**

Open the link (or `index.html`) in the Quest browser and choose **Play in passthrough** (or full VR). On a computer, open it in any modern browser and play with the mouse and keyboard. The controls are listed in the panel on the page.

## Files

| File | What it is |
| --- | --- |
| `index.src.html` | The game's source: one page of HTML, CSS and JavaScript (three.js) |
| `build.py` | Builds `index.html` by embedding everything in `assets/` into the page |
| `index.html` | The built game, ready to open: a single self-contained file |
| `assets/` | Hand models, the referee's and coach's voices, and the coach's lines |

## Building

```
python3 build.py
```

This reads `index.src.html`, embeds each `@@ASSET:name@@` file from `assets/` and writes `index.html`.

## Privacy

The published game at infidelus.github.io counts visits with [GoatCounter](https://www.goatcounter.com/), which uses no cookies and stores nothing that identifies anyone. Besides visits it records a few anonymous events, each at most once per visit: that a shot was played (and in which mode), and that the game was played in a headset. Nothing is counted when you run a downloaded copy, and the game works the same if a blocker stops the counter. Your settings and saved games stay in your own browser's local storage.

## Credits

- [three.js](https://threejs.org/) for 3D rendering.
- Hand models from the [WebXR Input Profiles](https://github.com/immersive-web/webxr-input-profiles) generic hand assets.
- The referees and coaches are made with [ElevenLabs](https://elevenlabs.io/) (Multilingual v2 model, on a paid plan), using voices from its voice library: **Mark** (male referee), **Olivia** (female referee), **Hamish** (male coach) and **Trinity X** (female coach). Numbers are written out in words, and each player's name is made in whole sentences such as "Lewis Ambrose to break".

## Licence

Desk Snooker is released under the [MIT Licence](LICENSE). Third-party parts keep their own licences: three.js, PeerJS and the WebXR Input Profiles hand models are MIT.

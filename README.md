# 🦖 ArticuSource

Welcome to **ArticuSource** — a *Jurassic-class* open-source collection of **articulated USD assets** for training robot learning models, building simulation pipelines, and experimenting in physics-rich environments.

Because your robot deserves *dino-mite* data.

---

## 🧬 What is ArticuSource?

ArticuSource is a fossil-free repository of **URDF-to-USD converted articulated assets**, designed for roboticists, ML researchers, and sim nerds who love building:

- Sim-to-real pipelines
- Reinforcement learning environments
- Isaac Sim or Omniverse USD-based setups
- Custom articulated agents with joint-level control

All assets are **open-source** and designed to be **modular**, **physically accurate**, and **ready for deep learning extinction events**.

---

## 🦴 What's Inside?

- 🦕 **USD Articulated Assemblies** – from simple joints to complex mechatronic dinos.
- 🦾 **Robot-Ready Constraints** – pre-configured with joint limits, damping, and stiffness.
- 🪨 **Prehistoric Performance** – tested in NVIDIA Omniverse (Isaac Sim / Isaac Lab).
- 🦖 **Dino Puns** – because every repo needs a little humor.
---

## 📦 Structure

```

articusource/
│
├── assets/
│   ├── tricerabot/         # 3DOF example asset
│   ├── raptarm/            # articulated manipulator
│   └── stegostacker/       # bin-picking dino-arm
│
├── configs/
│   └── physics\_presets.usda
│
├── scripts/
│   └── convert\_from\_urdf.py
│
└── README.md

````

---

## 🧠 Why Use ArticuSource?

Because why reinvent the (Jurassic) wheel?

- ✅ Speeds up sim setup
- ✅ Proven with RL frameworks
- ✅ Open license (MIT) — no amber DNA restrictions
- ✅ Dino puns included at no extra charge

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/Zenif-NIght/articu-source.git

# Open assets in Omniverse USD Composer or Isaac Sim
````

Want to train a T-RL agent? Just point it at one of the `/assets` and let the extinction events begin.

---

## 📜 License

MIT License — free to modify, distribute, and evolve (no cloning dinosaurs… yet).

---

## 🦕 Contributing

Got a new dino-bot? PRs welcome! Fork, add your asset, and make sure it doesn't bite.

---

## 🗺️ Roadmap

* [ ] Add RL-ready gym wrappers 🏋️
* [ ] Support procedural asset generation 🧬
* [ ] Publish a DinoZoo of articulated agents 🦖🦕

---

## 🧬 Fossil Fact

> Dinosaurs didn't have joints like these. But if they did, they'd be articulated and fully sim-ready.

---

Let’s make robot learning *prehistorically good*.

**– The ArticuSource Team**

* Christopher A.: Robot T-Rex Wrangler & Dino Data Scientist
* YOU TO can be part of this too!


If you found this repo useful, consider starring it on GitHub or sharing with your fellow robot/dino enthusiasts. if you use this in your projects or research, please cite it as:

```bibtex
@misc{articusource,
  author = {Allred, Christopher},
  title = {ArticuSource: Open-Source Articulated USD Assets for Robot Learning},
  year = {2025},
  url = {
    https://github.com/Zenif-NIght/articu-source
  }
}
```


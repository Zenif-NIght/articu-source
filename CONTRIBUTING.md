# 🦕 Contributing to ArticuSource

First off, thank you for considering contributing to **ArticuSource**! Your articulated asset, tool, or idea might just become the next *Rex* of robot learning.

---

## 🧰 What Can You Contribute?

We welcome contributions of all kinds, including:

- 🦾 **New articulated assets** (e.g., drawers, doors, robot arms)
- 🧪 **Simulation-ready USD files** with joints, collisions, and constraints
- 🐍 **Python utilities** (e.g., converters, validators, loaders)
- 🐛 **Bug reports** and 🛠️ **fixes**
- 📖 **Documentation** improvements or tutorials

---

## 🦴 Asset Contribution Guidelines

1. **USD Format**  
   - Use Omniverse Composer or Isaac Sim to author USD assets.
   - Assets must be hierarchical (e.g., `Xform` structure) and jointed where applicable.

2. **Physics Setup**
   - Include proper joint configuration: limits, damping, stiffness.
   - Add collision shapes and mass properties.

3. **Naming**
   - Use clear names: e.g., `Revolute_Hinge`, `Slider_Drawer`.
   - Prefix asset folders with a descriptive ID (e.g., `Gripper_X`, `Door_Classic`).

4. **Testing**
   - Test your asset in simulation (e.g., Isaac Sim).
   - Ensure it loads without warnings or errors.

5. **Documentation**
   - Provide a README.md in the asset folder with:
     - Asset description
     - Features and use cases
     - Example usage instructions
     - Screenshots or videos if possible
     - Asset structure diagram (optional)
     - include a license
     - Lastly add a Dino pun or two for fun!

---

## 🧪 Dev Environment Setup

```bash
# Clone the repo
git clone https://github.com/your-org/articusource.git
cd articusource

# Install any dev requirements (optional)
pip install -r requirements.txt
````

---

## 📦 Submitting a Pull Request

1. Fork this repo and create your feature branch:

   ```bash
   git checkout -b feature/my-new-asset
   ```

2. Commit your changes:

   ```bash
   git commit -am "Add new articulated drawer asset"
   ```

3. Push to the branch:

   ```bash
   git push origin feature/my-new-asset
   ```

4. Open a pull request and fill out the PR template.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License unless otherwise specified.

---

## 🦖 Community Dino Rules

* Be respectful — we're all part of the same prehistoric herd.
* No gatekeeping (unless you're simulating one).
* Keep commits clean and meaningful (avoid `fix lol` and `squash before merge`).

---

Thanks again for helping us build a *Cretaceous-class* repository for robot learning!

– The ArticuSource Team


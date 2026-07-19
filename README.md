# 🔗 Website QR Code Generator

A simple, clean web app for turning any website address into a downloadable QR code — no sign-up, no ads, just paste a URL and go.

**Live app:** [qr-code-generator-n.streamlit.app](https://qr-code-generator-n.streamlit.app/)

## Scan to open the live app

<img src="live_app_qr.png" alt="QR code linking to the live Streamlit app" width="200" />

## 1. Purpose & Audience

This app is built for anyone who needs a fast, free way to generate a QR code for a website link — marketers adding a QR code to a flyer or business card, small business owners linking to their site or menu, developers testing links, or anyone who just wants to share a URL as a scannable image. No technical knowledge required.

## 2. Tech Stack & Key Features

**Stack**
- [Streamlit](https://streamlit.io/) — Python web app framework
- [segno](https://github.com/heuer/segno) — QR code generation
- [Pillow](https://python-pillow.org/) — image handling

**Features**
- Enter any website address (scheme is added automatically if missing, e.g. `example.com` → `https://example.com`)
- Instant QR code generation with medium error correction
- Preview the generated QR code in-app
- Download the QR code as a PNG
- Clean, custom-styled UI with a responsive layout

## 3. Running Locally

**Prerequisites:** Python 3.9+

```bash
# Clone the repository
git clone https://github.com/<your-username>/QR-code-generator.git
cd QR-code-generator

# (Optional but recommended) create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run qr_code_app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## 4. Deployment

This app is deployed on **[Streamlit Community Cloud](https://streamlit.io/cloud)**, which builds and hosts the app directly from this GitHub repository.

- **Production URL:** https://qr-code-generator-n.streamlit.app/
- **Hosting:** Streamlit Community Cloud (free tier)
- **CI/CD:** Streamlit Community Cloud auto-redeploys on every push to the `main` branch — no separate CI/CD pipeline is configured
- **Config:** No custom `.streamlit/config.toml` is included; the app uses Streamlit's default server settings

To deploy your own copy:
1. Fork or push this repo to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io/), sign in, and click "New app"
3. Point it at your repo, branch (`main`), and entry file (`qr_code_app.py`)
4. Deploy — Streamlit installs `requirements.txt` automatically

## 5. Troubleshooting

**The app shows a "Zzz" sleep screen**

Streamlit Community Cloud puts inactive apps to sleep after a period of no traffic. To start a sleeping app, simply visit your app's public URL in a web browser and click the **"Yes, get this app back up!"** button on the sleep page. The app will spin back up in a few seconds.

## 6. Branding

- **Primary color:** `#4f46e5` (indigo)
- **Accent color:** `#6366f1` (violet)
- **Background gradient:** `#c7d2fe → #e0e7ff → #f5f3ff → #ffffff`
- **Footer:** dark slate (`#1f2937`) with violet accent text (`#a5b4fc`)
- Sidebar includes a profile photo (`assets/ak11.png`) and developer credit

## 7. License & Contributing

Licensed under the [MIT License](LICENSE).

Contributions are welcome:
1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes and open a pull request

For bugs or feature requests, please open an issue on GitHub.

---

Made with ❤️ by Akram Elsayed

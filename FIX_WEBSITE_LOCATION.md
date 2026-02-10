# 🚨 Important Fix Required: Move Files to Root

Your website is currently live at:
**<https://teal-leopard-555500.hostingersite.com/frontend/>**

But your main domain `https://teal-leopard-555500.hostingersite.com/` shows a **403 Forbidden** error because the files are inside a subfolder.

---

## ✅ How to Fix (Takes 1 Minute)

1. **Log in to Hostinger File Manager**
2. Open the **`public_html`** folder.
3. You will see a folder named **`frontend`**. **Double-click to open it.**
4. **Select all files** inside (`index.html`, `styles.css`, `chatbot.js`, `config.js`, etc.).
5. Right-click and choose **Move**.
6. Change the destination path to just:
    `/public_html`
    (Remove `/frontend` from the path)
7. Click **Move**.

---

## 🚀 Result

After moving the files:

- Your website will work perfectly at **<https://teal-leopard-555500.hostingersite.com/>**
- The 403 error will disappear.

---

## ⚙️ Backend Configuration Note

Currently, your frontend is looking for a backend API.

- If you have deployed the Python backend to `public_html/api`, make sure `config.js` points to `https://teal-leopard-555500.hostingersite.com/api`.
- If you haven't deployed the backend yet, the chat bubbles won't get a response.

---
**Need help?**
If you want to deploy the backend too, follow the "Full Stack" instructions in `HOSTINGER_DEPLOYMENT.md`.

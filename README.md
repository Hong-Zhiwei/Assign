[README.md](https://github.com/user-attachments/files/28046617/README.md)
# **🐹 夢幻打地鼠 \- 進階挑戰版 (Dream Whack-a-Mole Advanced)**

這是一個基於 **HTML5、CSS3 (Tailwind CSS) 與原生 JavaScript** 開發的現代化打地鼠網頁遊戲。本遊戲專注於精美的視覺體驗、流暢的動畫回饋以及豐富有趣的動態核心邏輯。

## **🌟 遊戲完整特性**

### **1\. 視覺與動畫 (Visuals & Animations)**

* **平滑升降過渡**：使用 CSS transition 結合貝茲曲線 (cubic-bezier)，使地鼠冒出與縮回時如同彈簧般生動自然。  
* **打擊視覺反饋**：  
  * 地鼠被擊中時會立即**更換為受擊表情**（普通地鼠眼冒金星、黃金地鼠墨鏡歪斜、炸彈地鼠化為碎屑與灰燼）。  
  * 配合 CSS 關鍵幀動畫（keyframes）實作「震動位移」效果。  
  * 產生**打擊煙霧塵埃**與**浮動分數跳字**（如 \+10、+50 ✨、-20 💣）。  
* **毛玻璃效果 (Glassmorphism)**：遊戲計分板、說明卡片以及結算面板皆採用半透明磨砂玻璃質感，搭配動態漸層背景，極具現代科技感。

### **2\. 核心遊戲邏輯 (Core Mechanics)**

* **多樣化地鼠角色**：  
  * **普通地鼠 (Normal Mole)**：擊中得 ![][image1] 分，並能累積 Combo。  
  * **黃金地鼠 (Gold Mole)**：閃爍金色光芒、速度極快、一閃即逝，擊中可獲 ![][image2] 分並享有 Combo 加成。  
  * **炸彈地鼠 (Bomb Mole)**：點擊會導致大爆炸，扣除 ![][image3] 分並讓整個螢幕**閃爍紅光**、Combo 歸零。  
* **連擊系統 (Combo)**：  
  * 連續擊中地鼠會累積 Combo。  
  * **5 Combo 以上**：得分 ![][image4] 倍。  
  * **10 Combo 以上**：得分 ![][image5] 倍。  
  * 漏掉任何一隻地鼠或誤擊炸彈，Combo 將立即中斷。  
* **動態難度系統 (Dynamic Difficulty)**：  
  * 遊戲會隨著分數提升自動調整難度（等級 1 \~ 6）。  
  * 地鼠停留時間逐漸縮短（最快縮短至 ![][image6] ），且同時在場上出現的地鼠數量會變多。

### **3\. 完善的流程與儲存**

* **完整的遊戲生命週期**：包含「開始頁面」、「遊戲中」與「結算頁面」。  
* **最高分紀錄管理**：利用瀏覽器本地儲存（localStorage）技術自動記錄最高分，並於首頁與結算頁面即時呈現。  
* **高相容性操作**：同時支援 PC 端的鼠標與行動裝置的觸控點擊，無操作延遲。

## **🛠️ 專案技術棧**

* **前端架構**：HTML5 (語意標籤), CSS3 (自訂 Keyframes 動態效果)  
* **樣式工具**：[Tailwind CSS](https://tailwindcss.com/) (提供精美的響應式佈局與現代 UI 元件)  
* **圖形資產**：純程式碼繪製的響應式 **SVG 圖形** (地鼠表情與細節，免除外部載入圖片資源的煩惱)  
* **核心邏輯**：原生 JavaScript (ES6+), Web Storage API

## **🎵 音效支援與自訂說明**

本專案已在 whack-a-mole-advanced.html 原始碼中為您預留了極具彈性的音效播放介面，並採用了防崩潰的安全設計。

若您需要啟用真實音效，請依照以下步驟操作：

1. 準備您的音效檔案（例如 mp3、wav 或 ogg 格式）。  
2. 開啟 whack-a-mole-advanced.html 檔案，搜尋 class SoundEffectsManager 區塊（約在 JavaScript 起始處）。  
3. 將預留的空字串欄位替換為您的音訊檔案路徑：

this.audioSources \= {  
    whackNormal: 'assets/sounds/normal\_hit.mp3', // 打擊普通地鼠  
    whackGold: 'assets/sounds/gold\_hit.mp3',     // 打擊黃金地鼠  
    bombExplosion: 'assets/sounds/explosion.mp3',// 誤擊炸彈  
    comboUp: 'assets/sounds/combo\_level\_up.mp3', // 達成大連擊  
    gameStart: 'assets/sounds/start\_fanfare.mp3',// 遊戲開始  
    gameOver: 'assets/sounds/game\_over.mp3',     // 遊戲結束  
    whackMiss: 'assets/sounds/miss\_swing.mp3'    // 揮空或漏打  
};

## **🚀 快速上手指南**

本遊戲為**單網頁應用程式 (SPA)**，所有代碼、樣式、腳本皆整合在一個單一的 .html 檔案中，極易部署與分享。

### **本地執行**

1. 下載或複製本專案的 whack-a-mole-advanced.html 檔案。  
2. 在您的電腦上，直接用任何瀏覽器（如 Chrome, Safari, Edge, Firefox）雙擊打開該 HTML 檔案。  
3. 立即開始享受流暢的打地鼠遊戲！

### **部署到線上**

由於是靜態單網頁，您可以完全免費且快速地將它託管到以下平台：

* **GitHub Pages**：將檔案命名為 index.html 並推送到 GitHub 儲存庫即可啟用。  
* **Vercel / Netlify / Cloudflare Pages**：直接拖放檔案即可一鍵上線。

## **📋 遊戲數值參數調校 (自訂開發)**

如果您想進一步微調遊戲平衡性，您可以在原始碼的 const CONFIG 物件中進行修改：

* gameDuration (預設 30)：每次遊戲的限時（秒）。  
* baseMoleUpTime (預設 1000)：地鼠在 Level 1 時的基礎停留時間（毫秒）。  
* minMoleUpTime (預設 450)：極限難度下地鼠的最短停留時間（毫秒）。  
* spawnInterval (預設 750)：生成地鼠的基礎頻率間隔（毫秒）。

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAZCAYAAADe1WXtAAABPklEQVR4XmNgGAX0AIwyMjIq6IJIgFFZWVlMXl7eEshmRpdEB4xycnJaCgoKG4EaHqBLggBQTgEodwyIrwDxLCC+DRQyQFcHBsbGxqyioqI8QEONgQq/AvFDdDUgABT/B1TjgsTXBOK3QDwFyGVEUooA+AwFWQo1QBMmBmRLgtQC8VUpKSkRZPVwgM9QoJwS1ABJmBjUogMgPSC9yOrhgIChIDlchv4Hyvsiq4cDAob6Ut1QoJgn1Q2llfcxIkpdXZ0XyD8MxN9kZWVNkdXDAQFDBYHinxQVFfVhYiALoBY9AOZCaWT1MMAIzB0eQAW/gfgViI+uACj+DGj4fFBmAfGB6itBjgDS5uhqYTb+x4IPgMINSZ0TyEIgXg40KAJIfwNaEsqAxQEkAXFxcW5gELgBDY0HsdHlR8EooAEAAJSgcfj1Hs0nAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAZCAYAAADe1WXtAAABmUlEQVR4Xu2UO0sDQRSFdxEFUQvRGJNNssYUIWkUFhXBQkQF8QEigmBhZ29p7T8QsRBErGzzEwTBX6CVFgpBQbARTaH4+K6ZWSeTIAZMlwOH2XvuuXd2HruO00Sj4MIWU4hGox2e5/WYmoKbyWT6fN8fd6yaCkQikU5Mz6lUqsB4AA/hazKZXDJ9AwD9HF4o3xXSsOkJoZqKSbhL80XbIyD3QW7aiHPwEe455dX+QJpiDipEC2piaZDTGs8xeAsv4/F4r+n/U1Pyg6pBTGtqolP4UlUvyXQ6PUpyHu7LFjjWIUjRL00/q7ZMJVdMTYxwx1F7JUV1Na0FWRIswrSK5/6j6b1vnHa9y3e5a1uIm6aoGoTmWgeVzWa7iM9giTs9Ehbr2Sgq5PP5Nq375eW/oU9IzNhN/MSBDhkefaVuEomEp/VvUDDD2/brGEM7xnf7i0K7w3sUBEGrxNRsy+SMY6ZPwyVZJHnslz/Ra4oXRDdN6FPwAZ7gXWMs4Vu1fSHk54FpGa5TMGnnNeRHwxbM4tmQZzvfRBMNwBcWgHWPgzZzwwAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAZCAYAAADe1WXtAAABjklEQVR4Xu2TMUvDUBSFE1pBURHBGpqkTZoOpZNCEBEHQURwcBLRzd/hv3AQBAcdHZzdHETBxVVRdNGlg+AitKP1uzQv3oYqWOjWA4f37rn3nvfebWpZQwwSOc/z/DAMV4IgKGaTCna1Wp2lZol9LpvsAkVPsAHfYRvzHWRb16CF5G7hPTyGL0jzusbAJnlYLpeXtSjG8LFSqThK+6JuTcV1+CH9lr5AoVCYQLwSyl41tLRJUicGdVVThG/wwXXdGaMLbJ5wQPMR+7wRKWzCNvqmxKxRYpDOW12oST42uoFcvWt+cktdLOsfpunhv4KbL8Jn5hkYTZr6NhWjrKGAxo2+TKMomqLgEtPrbK6v58dxPBJ0vr1zMRdNxuD7vif7Xj9UrVabJL6BrVKptGD0FBjsiykmY4mUJz4xxZhOE38yljnTIwckB72aw1MgbskTevBOzFRdg/hUXiVxcpGmvOjHzeqeSw9e0DBqaolXg87f+Ax9l7XFIdtW5nP8NxzHGWcE65juyT6bH2KIAeAbp8OCFSdYLAQAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABX0lEQVR4Xu2UvUrEUBCFE0QRtJMQNf9BLFIJAQuxVBD8AbG0sbKw8xl8AwsLwcLeYm0Eu30IC0uFBUGwELRRdP1mTfQyBiXLFip74HDvnTkzZ7LcvZbVx1+E7fv+FOuATlTADoJg0lJa13VHPM8bM2Mm7DAMsziOT6MouoITWqDhOM4ouiZ8oLbBeggv4BMDrGm9lef5oBQhzhE9wusaRmeFgXBfvkbrvqAbI/kSqdO5b/HrjZIkmUW/DA/gnPXTRerS6BztRhnjMm1xbsM9jrYh/0RdoyoYPVow0fkOemSUUnsDX9kv6HwHdY34mXbR3VG3XcakrqhvE1819R+oaxS9/1mlYSPLsiGJGT2e2c/rGoHNhEsigLfsZ7RAmpqTsi6KGdpxQ3MCXypfBpm+bKLYlJtl6OR5uUzTdLoI2Zx3YAuzY9YjeM8AK5Ir63oGeUAxWIebGA7rfB99/HO8AQvndV7rVgXDAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABsUlEQVR4Xu2UvS9DYRTG2yAhkfhs0Hvb23aQmG9EQsJiYLAwGPwBFjPxXxgkEglisGCVGETEqGuljYnFIDGQMBjU71TfOj1K6Eb6JE/ufc95zsd93/PeSKSBv4Qmz/P8VCo1EQTBgKyt4DsQ10ncaBiGLdZXBUQFeAvvYBE+YI5anYXv+91o9+E13IL3cNrqBFEc68lkckwbsS3BfDqd7tN2Db5iCs0rz0Vni8fjvdguyXdME20VcSwWa8dxJpR3Z08kEsOShIDJitgA347VqHzyZUNaH6WjNcQbvDc7I+sQYZHnzIe0Gviz8Em02k6+3a9i5SyqzkO6rJVEA/9NLY0qtKLtn4BwRBJwPoH1aYim7kKSHOEVwpz1WaB5rKtQJpPpQHCC8Bz2W79FXVsnFw3nJjyQgmKTLWREPat1CGoPg1yXPSkEZ5X9HSRdlUJ69llvy5hrnQb+w3LCygVV420bKAXMlQMss4i7lK5kd2PLL6uHBi9kq9UuzKN5kaeLK0F1YIsIjwhodVrWOVgg6aCyDcE8PIUL8JlGliO//Ff+CHK+TOu4FJKvtP4GGvjneAP9p46ABESguQAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE0AAAAZCAYAAAB0FqNRAAADcklEQVR4Xu1Xv2tUQRC+YBRBRVDj4eXuNnkBQ2JhcaBYqeAPRBQkWllYCiLaRWxEyN+gRaysbFMIglocpBEsTKEWgkUsDAo24gVUon7f3UwyGfa9excSUXgfDPv225nZ2e92970rlQoUKGAQQthXr9dveT4LjIHNw37DWkmS7Pc+Q0NDD2me/y/AwmVxa7aBgYHtzBVWxKI1Y6LgBzhHPxWNsTG/noAEd5nUUP2VSmUP2j7DlRqNxmbn14YUfmRkZGRvycX8TaTtJOXsOIWnmKs9c0KEaCFBQznz632DPYdNw17AvsPvjo1HEUfBvxIftm/seBZ4BFl8L5Z1bGOiBVmLHwfXpOmOzQ0UcABJ3oW4aG9DR4hpjF0ql8vbbCzQj7FHsAVLoj9GnuOWj0FEy1U4fejrRUsTXsXheGynaT4vciYk6DGS3gxx0eYs5xE64nyBvbQ8jzW4BcQmlo8hbcFZ5kVTBNlRVgQjdPsY+p1InjGMVS4LfQiYhPM93EO1sAbRZEIupGl5KZT8GctvNEw9y3eVF8WLJuucV/9MDA8PH4Lz7ODgYFUCo6KJ31nYfSbm/ac+Zpc0lSNUNBR31fIWa9lh3nzO0LmjdLwVO85etF7Qh2RTbNkJEdFGR0d3gHsGm1AOz8dhPzHpU/a7iWaLTYMuTPJELU8e+LW/61SUtE8KLxrXDJvpeqci6DB22G7tc8LgRItB/LjVf7G/HqLFoPN4PgtWKBWFdTGX99Nxf9+lgmLpTlHkFU123ywFYX+jROMiJG+arbq41Z/PfidlQerv/uaWCZbQflBD/6MU81m4E3ieCp0342WNtUfJ5GJcc3mCFb+uH44Z4nCO3DuNi9cfqBfRMMdcyPPWRMKtdLQG7jTaRWnZp0/7PxyKmRkfH9/CWLwUyuDek5f+QTx/De5jVvwo+Jjl80Lqyi2aRV7R6p27LPNkZYEvBV7wi2zZJ4nnCdiTarW6i33518APXQo5qcG1Wu08uCWNY4uib8PnpPrEwJ3BXN6E7yoa5jjmOSJLNIqEvK208VzIKJzHimJeh33iJGhfw35g7AbGNpk09LsGe4Cxi2xhi+SNT08IOURj7bG7KE00WWv3+2s9IEftAtpTSZLs9OMKCo1ir9Av8nerZ6T9oNZ8DGFFY03qy3zet0CBAgUKFChQ4B/CHylfyzjRBHTFAAAAAElFTkSuQmCC>

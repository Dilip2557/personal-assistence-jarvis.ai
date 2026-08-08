# UI Upgrade — Super Premium Dashboard

- [ ] Rewrite `dashboard/static/app.html` with a super-premium glass/gradient theme
  - [ ] Improve CSS: background gradients/aurora, glass blur surfaces, better typography, refined shadows/borders
  - [ ] Keep all existing UI functionality: feed rendering, websocket, encryption badge, file upload cards, mic voice streaming, footer actions, toast
  - [ ] Add small UX improvements: premium toast animation + optional smarter auto-scroll

- [ ] Rewrite `dashboard/static/login.html` with the same premium visual language
  - [ ] Improve CSS: glass card, gradient background, better focus/selection, refined shake animation
  - [ ] Keep existing login functionality and reconnection logic

- [ ] Quick manual verification
  - [ ] Login flow `/login` → redirect `/`
  - [ ] Websocket feed updates messages
  - [ ] SEND / WAKE actions still call backend correctly
  - [ ] File upload progress cards render and download links work
  - [ ] Microphone toggle still works (and voice setup prompt behavior unchanged)

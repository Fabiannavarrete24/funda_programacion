const pacman = document.querySelector('#pacman-loading img');
let pacmanPosition = 0;
let pacmanDirection = 1;
const pacmanSpeed = 3;

function animatePacman() {
  pacmanPosition += pacmanDirection * pacmanSpeed;
  if (pacmanPosition >= window.innerWidth - pacman.clientWidth || pacmanPosition <= 0) {
    pacmanDirection = -pacmanDirection;
  }
  pacman.style.left = pacmanPosition + 'px';
  requestAnimationFrame(animatePacman);
}

animatePacman();
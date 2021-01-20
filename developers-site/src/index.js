import './css/developers.scss';
import LazyLoad from 'vanilla-lazyload';
const lazyLoader = new LazyLoad({
  elements_selector: 'img[data-src]'
});

document.addEventListener('DOMContentLoaded', () => {
  console.log('developers page JS...');
}, true);

//add or remove query parameters you want to transfer
var queryParams = [
  'utm_medium',
  'utm_source',
  'utm_campaign',
  'utm_content',
  'utm_keyword',
  'utm_matchtype',
  'campaign_id',
  'ad_group_id',
  'ad_id',
  'gclid',
  'first_name',
  'last_name',
  'name',
  'full_name',
  'contact_id',
  'phone',
  'email',
];
var keys_to_map = {
  iframe: ['src', 'data-src'],
  a: 'href'
}; //change a href with data-href or other if url store in different attribute
function fetchParams() {
  decorateUrl().then(t => {
    Object.keys(keys_to_map).forEach(p => {
      var links = document.querySelectorAll(p);
      var key = keys_to_map[p];
      links.forEach(x => {
        if (!Array.isArray(key)) {
          key=[key];
        }
        key.forEach((item, i) => {
          var src = x.getAttribute(item);
          if (typeof src != 'undefined') {
            if (!src.includes('base64') && !src.includes('tel') && !src.includes('mail') && !src.includes('void') && !src.includes('javascript')) {
              src = src.replaceAll('#', '');
              src += (src.includes('?')) ? '&' : '?';
              src += t;
              item = item.replaceAll('data-','');
              x.setAttribute(item, src);
            }
          }
        });
      });
    })
  }).catch(err => {

  })


  function getQueryParam(name) {
    if (name = (new RegExp('[?&]' + encodeURIComponent(name) + '=([^&]*)')).exec(window.location.search))
      return decodeURIComponent(name[1]);
  }

  function decorateUrl(urlToDecorate = '') {

    return new Promise((resolve, reject) => {

      var keyparam = 'url_params';
      var collectedQueryParams = ['source='+location.hostname];//[];
      var objectaparams = localStorage.getItem(keyparam) || {
        source: location.hostname
      };
      if (typeof objectaparams == 'string') {
        objectaparams = JSON.parse(objectaparams);
      }
      queryParams.forEach((t, index) => {
        var value = getQueryParam(t);
        if (typeof value != 'undefined') {
          objectaparams[t] = value;
        } else {
          value = objectaparams[t] ?? '';
        }
        if (value != '') {
          collectedQueryParams.push(t + '=' + value);
        }
        if (index == queryParams.length - 1) {
          localStorage.setItem(keyparam, JSON.stringify(objectaparams));
          if (collectedQueryParams.length > 0) {
            var params = collectedQueryParams.join('&');
            if (urlToDecorate != '') {
              try {
                urlToDecorate = urlToDecorate.replaceAll('#', '');
                urlToDecorate += (urlToDecorate.includes('?')) ? '&' : '?';
                params = urlToDecorate + params;
              } catch (e) {

              }
            }
            resolve(params);
          }
          reject('');
        }
      });
    });

  }
}
document.addEventListener('readystatechange', event => {

  // When HTML/DOM elements are ready:
  if (event.target.readyState === "interactive") { //does same as:  ..addEventListener("DOMContentLoaded"..

  }

  // When window loaded ( external resources are loaded too- `css`,`src`, etc...)
  if (event.target.readyState === "complete") {
    console.log('fetching params');
    fetchParams();
  }
});

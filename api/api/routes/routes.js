'use strict';
module.exports = function(app) {
  var ips = require('../controllers/ipController');

  app.route('/ips')
    .get(ips.list_all_ips)
    .post(ips.create_an_ip);

  app.route('/ips/:ipId')
    .get(ips.read_an_ip)
    .delete(ips.delete_an_ip);
};

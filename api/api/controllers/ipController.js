'use strict';
var mongoose = require('mongoose'),
  Ip = mongoose.model('Ips');

exports.list_all_ips = function(req, res) {
  Ip.find({}, function(err, ip) {
    if (err)
      res.send(err);
    res.json(ip);
  });
};

exports.create_an_ip = function(req, res) {
  var new_ip = new Ip(req.body);
  new_ip.save(function(err, ip) {
    if (err)
      res.send(err);
    res.json(ip);
  });
};

exports.read_an_ip = function(req, res) {
  Ip.findById(req.params.ipId, function(err, ip) {
    if (err)
      res.send(err);
    res.json(ip);
  });
};

exports.delete_an_ip = function(req, res) {
  Ip.remove({
    _id: req.params.ipId
  }, function(err, ip) {
    if (err)
      res.send(err);
    res.json({ message: 'Ip successfully deleted' });
  });
};

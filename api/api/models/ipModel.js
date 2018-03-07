'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var IpSchema = new Schema({
  ip: {
    type: String,
    required: 'Enter IP'
  },
  created_date: {
    type: Date,
    default: Date.now
  },
});

module.exports = mongoose.model('Ips', IpSchema);

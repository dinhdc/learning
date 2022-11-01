const mongoose = require("mongoose");


const BranchSchema = new mongoose.Schema({
    name: String,
    area: String
}, {
    toJSON: { virtuals: true },
    toObject: { virtuals: true }
})


BranchSchema.virtual('id', {
    id: this.id
});

const BranchModel = mongoose.model('Branch', BranchSchema);

module.exports = BranchModel;
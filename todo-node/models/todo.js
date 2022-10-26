const mongoose = require('mongoose');
const TodoSchema = new mongoose.Schema({
    id: String,
    task: String,
    status: {
        type: String,
        enum: ['Active', 'Deactive', 'Completed']
    },
    createdAt: {
        type: Date,
        default: Date.now
    },
    dealine: Date,
    note: String,
    updatedAt: Date
});

TodoSchema.pre('save', function (next) {
    this.id = this._id;
    next();
});

const TodoModel = mongoose.model('Todo', TodoSchema);

module.exports = TodoModel;
const exporess = require('express');
const BranchModel = require('../models/Branch');

const branchRouter = exporess.Router();

branchRouter.get('/', async (req, res) => {
    try {
        const branches = await BranchModel.find();
        if (branches) {
            res.status(200).json(branches)
        }
        res.status(400);
    } catch (err) {
        res.sendStatus(400)
    }
})

branchRouter.post('/', async (req, res) => {
    try {
        const data = req.body;
        const branch = await BranchModel.create(data);
        res.status(201).json(branch)
    } catch (err) {
        res.status(400)
    }
})


branchRouter.get('/:id', async (req, res) => {
    try {
        const id = req.params.id
        const branch = await BranchModel.findById(id);
        if (branch) {
            res.status(200).json(branch)
        }
        res.status(400);
    } catch (err) {
        res.sendStatus(400)
    }
})


branchRouter.put('/:id', async (req, res) => {
    try {
        const id = req.params.id
        const body = req.body;
        const branch = await BranchModel.findByIdAndUpdate(id, body);
        if (branch) {
            res.sendStatus(200)
        }
        res.status(400);
    } catch (err) {
        res.sendStatus(400)
    }
})


branchRouter.delete('/:id', async (req, res) => {
    try {
        const id = req.params.id
        const branch = await BranchModel.findByIdAndDelete(id);
        res.sendStatus(204)
    } catch (err) {
        res.status(400)
    }
})

module.exports = branchRouter;
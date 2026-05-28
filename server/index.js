const express = require('express');
const mongoose = require('mongoose');
const itemModel = require('./schema/Item')
const cors = require('cors');
require('dotenv').config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

app.get('/api/items', async (req, res) => {
  const items = await itemModel.find();
  res.json(items);
});

app.delete('/api/items/:id', async (req, res) => {
  try {
    await itemModel.findByIdAndDelete(req.params.id);
    res.json({success:true});
  } catch (err) {
    console.log(err);
    res.status(500).json({error:"couldnt delte itm"});
  }
});

app.post('/api/items', (req, res) => {
  const { name, email, password } = req.body;
  console.log(`Name = ${name} Email= ${email} Password = ${password}`);
  let newItem = new itemModel({
    name: name,
    email: email,
    password: password
  });
  newItem.save()
    .then(doc => {
      console.log("account saved");
      res.json(doc);
    })
    .catch(err => {
      console.log(err);
      res.status(500).json({ error: "Failed to save item" });
    });
});
// Database Connection
const PORT = process.env.PORT || 5000;

mongoose.connect(process.env.MONGO_URI)
  .then(() => {
    console.log("MongoDB Connected");
    app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
  })
  .catch(err => console.log("DB Connection Error:", err));
  
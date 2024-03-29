/* 
    Title: tran-Aggregate-Queries.js
    Author: Phuong Tran
    Date: 16/02/2024
    Description: MongoDB aggregate queries.
*/

// display all documents from the collection
db.houses.find().forEach(printjson);
// display all documents from the collection
db.students.find().forEach(printjson);

// create a new document
db.students.insertOne({
  firstName: 'Phuong',
  lastName: 'Tran',
  studentId: 's9999',
  houseId: 'h1007'
});

// find a specific document
db.students.find({
  firstName: 'Phuong',
  lastName: 'Tran'
})
.forEach(printjson);

// delete a specific document
db.students.deleteOne({
  firstName: 'Phuong',
  lastName: 'Tran',
  studentId: 's9999',
  houseId: 'h1007'
});

// look up a specific document
db.students.find({
  firstName: 'Phuong',
  lastName: 'Tran'
})
.forEach(printjson);

// create lists of student arranged by house
let studentByHouse = 
  db.houses.aggregate({
    $lookup: 
      {
        from: 'students',
        localField: 'houseId',
        foreignField: 'houseId',
        as: 'studentsInThisHouse'
      }
  });
// display the list of students by house
print(studentByHouse);

// create lists of student arranged by founder
let Gryffindor = 
  db.houses.aggregate(
    {$match: {founder: 'Godric Gryffindor'}},
    {$lookup: 
      {
        from: 'students',
        localField: 'houseId',
        foreignField: 'houseId',
        as: 'studentsInThisHouse'
      }
    }
  );
// display the list of students by founder
print(Gryffindor);

// create lists of student arranged by mascot
let Eagle = 
  db.houses.aggregate(
    {$match: {mascot: 'Eagle'}},
    {$lookup: 
      {
        from: 'students',
        localField: 'houseId',
        foreignField: 'houseId',
        as: 'studentsInThisHouse'
      }
    }
  );
// display the list of students by mascot
print(Eagle);

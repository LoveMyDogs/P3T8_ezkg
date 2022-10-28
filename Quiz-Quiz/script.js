let question = {
    title:'gato', 
    alternatives: ['dog','cat', 'bird','fish']
    correctAnswer: 1 
};

function showQuestion(q) {
    // 1. select dom element 
    let titleDiv = document.getElementById('title');

    // 2. modify it 
    titleDiv.textContent = q. title;

    // selecting by a query
    let alts = document.querySelectorAll('alternatives')
    alts.forEach(sunction(element, index){
        element.textContext = q.alternatives[index];

        element. addEventListener('click', function(){
            // check correct answer 
            if(q.correctAnswer == index)
        });
    });
}

showQuestion(question);

let btn = document.getElementById('btn');

btn.addEventListener('click', function(){
    console.log('Clicked!');
});








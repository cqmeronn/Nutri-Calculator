document.addEventListener('DOMContentLoaded', function() {
    updateUnitLabels();
});

document.getElementById('unit-system').addEventListener('change', function() {
    updateUnitLabels();
});

function updateUnitLabels() {
    const unitSystem = document.getElementById('unit-system').value;
    const weightLabel = document.querySelector('label[for="weight"]');
    const heightLabel = document.querySelector('label[for="height"]');

    if (unitSystem === 'metric') {
        weightLabel.textContent = 'Weight (kg):';
        heightLabel.textContent = 'Height (cm):';
    } else {
        weightLabel.textContent = 'Weight (lbs):';
        heightLabel.textContent = 'Height (inches):';
    }
}

function calculate() {
    const unitSystem = document.getElementById('unit-system').value;
    const gender = document.getElementById('gender').value;
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    const age = parseInt(document.getElementById('age').value);
    const activityLevel = parseInt(document.getElementById('activity-level').value);
    const goal = parseInt(document.getElementById('goal').value);
    let weightChange = null;

    if (goal === 2 || goal === 3) {
        weightChange = parseInt(document.getElementById('weight-change').value);
    }

    if (unitSystem === 'imperial') {
        const weightInKg = weight * 0.453592;
        const heightInCm = height * 2.54;
        calculateBMR(gender, weightInKg, heightInCm, age, activityLevel, goal, weightChange);
    } else {
        calculateBMR(gender, weight, height, age, activityLevel, goal, weightChange);
    }
}

function calculateBMR(gender, weight, height, age, activityLevel, goal, weightChange) {
    let bmr;
    if (gender === 'male') {
        bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age);
    } else {
        bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age);
    }

    const activityMultipliers = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    };

    let totalCalories = Math.round(bmr * activityMultipliers[activityLevel]);

    if (goal === 2) {
        const calorieDeficits = { 1: 300, 2: 500, 3: 1100 };
        totalCalories -= calorieDeficits[weightChange];
    } else if (goal === 3) {
        const calorieSurpluses = { 1: 300, 2: 500, 3: 1100 };
        totalCalories += calorieSurpluses[weightChange];
    }

    displayResults(bmr, totalCalories);
}

function displayResults(bmr, totalCalories) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <h2>Results</h2>
        <p>Your BMR is: ${Math.round(bmr)} kcal/day</p>
        <p>Your total daily calorie needs are: ${totalCalories} kcal/day</p>
    `;
}

document.getElementById('goal').addEventListener('change', function() {
    const weightChangeContainer = document.getElementById('weight-change-container');
    if (this.value === '2' || this.value === '3') {
        weightChangeContainer.style.display = 'block';
    } else {
        weightChangeContainer.style.display = 'none';
    }
});

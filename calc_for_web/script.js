document.getElementById('unit-system').addEventListener('change', function() {
    const formContainer = document.getElementById('form-container');
    if (this.value) {
      formContainer.classList.remove('hidden');
      formContainer.classList.add('visible');
      updateUnitLabels();
    } else {
      formContainer.classList.remove('visible');
      formContainer.classList.add('hidden');
    }
  });
  
  document.addEventListener('DOMContentLoaded', function() {
    updateUnitLabels();
  });
  
  function updateUnitLabels() {
    const unitSystem = document.getElementById('unit-system').value;
    const weightLabel = document.querySelector('label[for="weight"]');
    const heightLabel = document.querySelector('label[for="height"]');
  
    if (unitSystem === 'metric') {
      weightLabel.textContent = 'Weight (kg):';
      heightLabel.textContent = 'Height (cm):';
    } else if (unitSystem === 'imperial') {
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
  
    const errorMessage = document.getElementById('error-message');
    const formContainer = document.getElementById('form-container');
  
    const inputs = document.querySelectorAll('#form-container input, #form-container select');
    let isValid = true;
    inputs.forEach(input => {
      if (!input.value) {
        input.classList.add('error');
        isValid = false;
      } else {
        input.classList.remove('error');
      }
    });
  
    if (!unitSystem || !gender || isNaN(weight) || isNaN(height) || isNaN(age) || isNaN(activityLevel) || isNaN(goal)) {
      errorMessage.classList.remove('hidden');
      errorMessage.classList.add('visible-error');
      formContainer.classList.add('shake');
      setTimeout(() => {
        formContainer.classList.remove('shake');
      }, 500);
      isValid = false;
    } else {
      errorMessage.classList.add('hidden');
      errorMessage.classList.remove('visible-error');
    }
  
    if (!isValid) {
      return;
    }
  
    if (unitSystem === 'imperial') {
      const weightInKg = weight * 0.453592;
      const heightInCm = height * 2.54;
      calculateBMR(gender, weightInKg, heightInCm, age, activityLevel, goal, weightChange);
    } else {
      calculateBMR(gender, weight, height, age, activityLevel, goal, weightChange);
    }
  
    const formWrapper = document.getElementById('form-wrapper');
    formWrapper.classList.remove('expanded');
    formWrapper.classList.add('collapsed');
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
      const deficits = { 1: 300, 2: 500, 3: 1100 };
      totalCalories -= deficits[weightChange];
    } else if (goal === 3) {
      const surpluses = { 1: 300, 2: 500, 3: 1100 };
      totalCalories += surpluses[weightChange];
    }
  
    totalCalories = Math.round(totalCalories / 100) * 100;
  
    displayResults(bmr, totalCalories);
  }
  
  function displayResults(bmr, totalCalories) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
      <h2 style="margin-bottom: 1rem;">Here are your results!</h2>
      <p style="margin-bottom: 1rem;">
        Your Basic Metabolic Rate is: <strong>${Math.round(bmr)} kcal/day</strong>
      </p>
      <p style="margin-bottom: 1rem;">
        Your total daily calorie needs are: <strong>${totalCalories} kcal/day</strong>
      </p>
  
      <!-- Add the "Start Again!" button -->
      <button type="button" onclick="startAgain()" style="padding: 10px 20px; margin-top: 1rem;">
        Start Again!
      </button>
    `;
  }
  
  function startAgain() {
    document.getElementById('results').innerHTML = '';
  
    document.getElementById('calculator-form').reset();
  
    const errorMessage = document.getElementById('error-message');
    errorMessage.classList.add('hidden');
    errorMessage.classList.remove('visible-error');
  
    document.getElementById('form-container').classList.remove('visible');
    document.getElementById('form-container').classList.add('hidden');
    document.getElementById('unit-system').value = '';
  
    const formWrapper = document.getElementById('form-wrapper');
    formWrapper.classList.remove('collapsed');
    formWrapper.classList.add('expanded');
  }
  

  
  
  document.getElementById('goal').addEventListener('change', function() {
    const weightChangeContainer = document.getElementById('weight-change-container');
    if (this.value === '2' || this.value === '3') {
      weightChangeContainer.classList.remove('hidden');
      weightChangeContainer.classList.add('visible');
    } else {
      weightChangeContainer.classList.remove('visible');
      weightChangeContainer.classList.add('hidden');
    }
  });
  
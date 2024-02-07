import { useState } from 'react';

const choices = ['Rock', 'Paper', 'Scissors'];

const Chooser = () => {
  const [choice, setChoice] = useState(0);

  const nextChoice = () => {
    setChoice((choice + 1) % choices.length);
  }

  return (
    <button onClick={nextChoice}>{choices[choice]}</button>
  );
};

export default Chooser;
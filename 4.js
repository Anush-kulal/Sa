import React, { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  const [step, setStep] = useState(1);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Count: {count}</h1>
      <input type="number" value={step} onChange={(e) => setStep(Number(e.target.value))} min="1" />
      <button onClick={() => setCount(count + step)}>Increase</button>
      <button onClick={() => setCount(Math.max(0, count - step))}>Decrease</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
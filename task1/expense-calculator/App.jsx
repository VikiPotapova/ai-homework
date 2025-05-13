import React, { useState } from 'react';

function App() {
  const [expenses, setExpenses] = useState([]);
  const [category, setCategory] = useState('');
  const [amount, setAmount] = useState('');
  const [results, setResults] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!category || !amount) return;

    const newExpense = {
      id: Date.now(),
      category: category.trim(),
      amount: parseFloat(amount)
    };

    setExpenses([...expenses, newExpense]);
    setCategory('');
    setAmount('');
  };

  const calculateResults = () => {
    const totalExpenses = expenses.reduce((sum, expense) => sum + expense.amount, 0);
    const averageDaily = totalExpenses / 30;
    const topExpenses = [...expenses]
      .sort((a, b) => b.amount - a.amount)
      .slice(0, 3);

    setResults({
      total: totalExpenses,
      average: averageDaily,
      topExpenses: topExpenses
    });
  };

  return (
    <div className="container">
      <div className="header">
        <h1>Expense Calculator</h1>
      </div>

      <form onSubmit={handleSubmit} className="expense-form">
        <div className="input-group">
          <input
            type="text"
            className="input-field"
            placeholder="Category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
          />
          <input
            type="number"
            className="input-field"
            placeholder="Amount ($)"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            min="0"
            step="0.01"
          />
          <button type="submit" className="button">Add Expense</button>
        </div>
      </form>

      {expenses.length > 0 && (
        <>
          <table className="expense-table">
            <thead>
              <tr>
                <th>Category</th>
                <th>Amount ($)</th>
              </tr>
            </thead>
            <tbody>
              {expenses.map(expense => (
                <tr key={expense.id}>
                  <td>{expense.category}</td>
                  <td>${expense.amount.toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <button onClick={calculateResults} className="button">
            Calculate
          </button>
        </>
      )}

      {results && (
        <div className="results">
          <h2>Results</h2>
          <p>Total amount of expenses: ${results.total.toFixed(2)}</p>
          <p>Average daily expense: ${results.average.toFixed(2)}</p>
          <h3>Top 3 Expenses:</h3>
          <ul className="top-expenses">
            {results.topExpenses.map(expense => (
              <li key={expense.id}>
                {expense.category}: ${expense.amount.toFixed(2)}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App; 
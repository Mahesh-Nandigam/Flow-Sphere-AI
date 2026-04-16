import React from 'react';

const ActionLogs = ({ logs }) => {
  // Use mock logs if empty to demonstrate XAI
  const displayLogs = logs.length > 0 ? logs : [
    { id: 1, type: 'urgent', text: "Gate 3 congested because density ↑ 40% in 2 mins. Action: Throttling inflow.", time: new Date().toLocaleTimeString() },
    { id: 2, type: 'success', text: "Redirecting Swarm Group A to Gate 5 because wait time ↓ 60%.", time: new Date().toLocaleTimeString() },
    { id: 3, type: 'warning', text: "Minor density spike detected near Concession Stand 4. Monitoring.", time: new Date().toLocaleTimeString() },
    { id: 4, type: 'success', text: "Dynamic Graph Optimization Complete. All active agents have new paths.", time: new Date().toLocaleTimeString() }
  ];

  return (
    <div 
      style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem', marginTop: '1rem' }}
      role="log" 
      aria-live="polite" 
      aria-atomic="false"
    >
      {displayLogs.map(log => (
        <div key={log.id} className={`log-entry ${log.type}`}>
          <span>{log.text}</span>
          <span className="log-time">{log.time}</span>
        </div>
      ))}
    </div>
  );
}

export default ActionLogs;

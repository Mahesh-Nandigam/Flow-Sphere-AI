import React from 'react';

const ControlPanel = ({ gates }) => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', marginTop: '1rem' }}>
      
      <div className="control-section">
        <h3 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginBottom: '0.75rem' }}>Gate API Status</h3>
        {Object.entries(gates).map(([gateName, data]) => (
          <div key={gateName} style={{ 
              display: 'flex', 
              justifyContent: 'space-between', 
              alignItems: 'center',
              padding: '0.75rem',
              background: 'rgba(0,0,0,0.2)',
              borderRadius: '8px',
              marginBottom: '0.5rem',
              borderLeft: data.status === 'throttled' ? '3px solid var(--accent-red)' : '3px solid var(--accent-green)'
            }}>
            <div>
              <div style={{ fontWeight: '600' }}>{gateName}</div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Status: {data.status.toUpperCase()}</div>
            </div>
            <div style={{ textAlign: 'right' }}>
              <div style={{ fontWeight: '600', color: data.load > 0.8 ? 'var(--accent-red)' : 'var(--text-primary)' }}>
                {(data.load * 100).toFixed(0)}% Load
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="control-section">
        <h3 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginBottom: '0.75rem' }}>Smart LED Signboards</h3>
        
        <div style={{ padding: '0.75rem', background: '#000', borderRadius: '4px', border: '1px solid #334155', fontFamily: 'monospace', color: 'var(--accent-green)', letterSpacing: '1px' }}>
          &gt; ROUTE A: CLEAR<br/>
          &gt; PLEASE PROCEED TO GATE 5<br/>
        </div>
      </div>
      
      <button style={{
        marginTop: '1rem',
        padding: '0.75rem',
        background: 'rgba(239, 68, 68, 0.1)',
        border: '1px solid rgba(239, 68, 68, 0.3)',
        color: 'var(--accent-red)',
        borderRadius: '8px',
        cursor: 'pointer',
        fontWeight: 'bold',
        textTransform: 'uppercase',
        letterSpacing: '1px',
        transition: 'all 0.2s'
      }}>
        ENGAGE EMERGENCY OVERRIDE
      </button>

    </div>
  );
}

export default ControlPanel;

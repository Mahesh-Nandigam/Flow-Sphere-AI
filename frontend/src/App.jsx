import React, { useState, useEffect } from 'react';
import LivingMap from './components/LivingMap';
import ActionLogs from './components/ActionLogs';
import ControlPanel from './components/ControlPanel';
import { Activity, ShieldAlert, Users } from 'lucide-react';

function App() {
  const [simulationData, setSimulationData] = useState({
    agents: [],
    gates: {},
    logs: []
  });

  // Real WebSocket connection to FastAPI
  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws');
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setSimulationData(data);
    };

    ws.onclose = () => {
      console.log('WebSocket Disconnected');
    };

    return () => ws.close();
  }, []);

  return (
    <div className="command-center" role="region" aria-label="Stadium Flow Control Dashboard">
      <header className="header">
        <h1>FlowSphere OS <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>// Control Center</span></h1>
        <div style={{ display: 'flex', gap: '2rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Users size={18} color="var(--accent-blue)" />
            <span>Active Agents: {simulationData.agents.length}</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Activity size={18} color="var(--accent-green)" />
            <span>System: ONLINE</span>
          </div>
        </div>
      </header>

      <aside className="panel" style={{ overflowY: 'auto' }}>
        <h2 className="panel-title">
          <Activity size={16} /> Explainable AI Logs
        </h2>
        <ActionLogs logs={simulationData.logs} />
      </aside>

      <main className="map-container">
        <LivingMap agents={simulationData.agents} />
      </main>

      <aside className="panel">
        <h2 className="panel-title">
          <ShieldAlert size={16} /> Infrastructure Control
        </h2>
        <ControlPanel gates={simulationData.gates} />
      </aside>
    </div>
  );
}

export default App;

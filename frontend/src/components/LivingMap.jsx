import React, { useRef, useEffect } from 'react';

const LivingMap = ({ agents }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear canvas
    ctx.fillStyle = '#0b0f19';
    ctx.fillRect(0, 0, width, height);

    // Draw Grid (Dynamic Map Feel)
    ctx.strokeStyle = 'rgba(59, 130, 246, 0.1)';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 40) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    for (let y = 0; y < height; y += 40) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    // Draw Mock Stadium Structures
    ctx.fillStyle = 'rgba(20, 27, 45, 0.8)';
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.lineWidth = 2;
    // Central Pitch
    ctx.beginPath();
    ctx.roundRect(width/2 - 200, height/2 - 120, 400, 240, 20);
    ctx.fill();
    ctx.stroke();

    // Draw Agents
    agents.forEach(agent => {
      ctx.beginPath();
      ctx.arc(agent.x, agent.y, 3, 0, Math.PI * 2);
      
      // Determine color based on density/status (mocked here based on status)
      if (agent.status === 'urgent') {
        ctx.fillStyle = '#ef4444'; // Red
      } else if (agent.status === 'warning') {
        ctx.fillStyle = '#eab308'; // Yellow
      } else {
        ctx.fillStyle = '#3b82f6'; // Blue
      }
      
      ctx.fill();
      
      // Add glowing effect
      ctx.shadowBlur = 10;
      ctx.shadowColor = ctx.fillStyle;
      ctx.fill();
      ctx.shadowBlur = 0; // Reset
    });

  }, [agents]);

  return (
    <canvas 
      ref={canvasRef} 
      width={1000} 
      height={800} 
      className="living-map"
      style={{ width: '100%', height: '100%', objectFit: 'contain' }}
    />
  );
};

export default LivingMap;

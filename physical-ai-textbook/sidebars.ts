import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'index', // homepage
    'intro',
    'introduction-to-physical-ai',
    'basics-of-humanoid-robotics',
    {
      type: 'category',
      label: 'Modules',
      items: [
        'module-01/index', // ROS 2 Fundamentals
        'module2/index',   // Digital Twin Simulation
        'module3/index',   // NVIDIA Isaac Platform
        'module4/index',   // Vision-Language-Action Systems
      ],
    },
    'capstone-ai-robot-pipeline',
  ],
};

export default sidebars;

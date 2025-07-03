import React from 'react'

export function Input({ className = '', ...props }) {
  return (
    <input
      className={`w-full px-4 py-2.5 border border-files-light-pink rounded-lg focus:outline-none focus:ring-2 focus:ring-files-primary-red/20 focus:border-files-primary-red transition-all duration-200 bg-white/80 backdrop-blur-sm ${className}`}
      {...props}
    />
  )
} 
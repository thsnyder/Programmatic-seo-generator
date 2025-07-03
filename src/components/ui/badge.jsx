import React from 'react'

export function Badge({ children, variant = 'default', className = '', ...props }) {
  const variantClasses = {
    default: 'bg-gradient-to-r from-files-primary-red to-files-bright-red text-white',
    secondary: 'bg-files-light-pink text-files-primary-red border border-files-super-light-red',
    outline: 'border border-files-light-pink text-files-headline-black bg-white'
  }
  
  return (
    <span
      className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium shadow-sm ${variantClasses[variant]} ${className}`}
      {...props}
    >
      {children}
    </span>
  )
} 
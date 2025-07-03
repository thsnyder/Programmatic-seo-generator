import React from 'react'

export function Button({ children, className = '', size = 'default', variant = 'default', ...props }) {
  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    default: 'px-4 py-2',
    lg: 'px-6 py-3 text-lg'
  }
  
  const variantClasses = {
    default: 'bg-gradient-to-r from-files-primary-red to-files-bright-red hover:from-files-maroon hover:to-files-primary-red text-white shadow-md hover:shadow-lg',
    outline: 'border border-files-light-pink text-files-headline-black hover:bg-files-light-pink',
    secondary: 'bg-files-light-pink text-files-primary-red hover:bg-files-super-light-red'
  }
  
  return (
    <button
      className={`inline-flex items-center justify-center rounded-lg font-medium transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-files-primary-red/20 disabled:opacity-50 disabled:cursor-not-allowed ${sizeClasses[size]} ${variantClasses[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  )
} 